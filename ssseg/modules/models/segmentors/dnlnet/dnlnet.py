'''
Function:
    Implementation of DNLNet
Author:
    Zhenchao Jin
'''
import copy
import torch
import torch.nn as nn
from ..base import BaseSegmentor
from .dnlblock import DisentangledNonLocal2d
from ...backbones import BuildActivation, BuildNormalization


'''DNLNet'''
class DNLNet(BaseSegmentor):
    def __init__(self, cfg, mode):
        super(DNLNet, self).__init__(cfg, mode)
        align_corners, norm_cfg, act_cfg, head_cfg = self.align_corners, self.norm_cfg, self.act_cfg, cfg['head']
        # build disentangled non-local block
        self.conv_before_dnl = nn.Sequential(
            nn.Conv2d(head_cfg['in_channels'], head_cfg['feats_channels'], kernel_size=3, stride=1, padding=1, bias=False),
            BuildNormalization(placeholder=head_cfg['feats_channels'], norm_cfg=norm_cfg),
            BuildActivation(act_cfg),
        )
        self.dnl_block = DisentangledNonLocal2d(
            in_channels=head_cfg['feats_channels'], reduction=head_cfg['reduction'], use_scale=head_cfg['use_scale'], mode=head_cfg['mode'], 
            temperature=head_cfg['temperature'], norm_cfg=copy.deepcopy(norm_cfg), act_cfg=copy.deepcopy(act_cfg),
        )
        self.conv_after_dnl = nn.Sequential(
            nn.Conv2d(head_cfg['feats_channels'], head_cfg['feats_channels'], kernel_size=3, stride=1, padding=1, bias=False),
            BuildNormalization(placeholder=head_cfg['feats_channels'], norm_cfg=norm_cfg),
            BuildActivation(act_cfg),
        )
        # build decoder
        self.decoder = nn.Sequential(
            nn.Conv2d(head_cfg['feats_channels'] + head_cfg['in_channels'], head_cfg['feats_channels'], kernel_size=3, stride=1, padding=1, bias=False),
            BuildNormalization(placeholder=head_cfg['feats_channels'], norm_cfg=norm_cfg),
            BuildActivation(act_cfg),
            nn.Dropout2d(head_cfg['dropout']),
            nn.Conv2d(head_cfg['feats_channels'], cfg['num_classes'], kernel_size=1, stride=1, padding=0)
        )
        # build auxiliary decoder
        self.setauxiliarydecoder(cfg['auxiliary'])
        # freeze normalization layer if necessary
        if cfg.get('is_freeze_norm', False): self.freezenormalization()
    '''forward'''
    def forward(self, x, targets=None):
        img_size = x.size(2), x.size(3)
        # feed to backbone network
        backbone_outputs = self.transforminputs(self.backbone_net(x), selected_indices=self.cfg['backbone'].get('selected_indices'))
        # feed to disentangled non-local block
        feats = self.conv_before_dnl(backbone_outputs[-1])
        feats = self.dnl_block(feats)
        feats = self.conv_after_dnl(feats)
        # feed to decoder
        feats = torch.cat([backbone_outputs[-1], feats], dim=1)
        predictions = self.decoder(feats)
        # forward according to the mode
        if self.mode == 'TRAIN':
            loss, losses_log_dict = self.customizepredsandlosses(
                predictions=predictions, targets=targets, backbone_outputs=backbone_outputs, losses_cfg=self.cfg['losses'], img_size=img_size,
            )
            return loss, losses_log_dict
        return predictions