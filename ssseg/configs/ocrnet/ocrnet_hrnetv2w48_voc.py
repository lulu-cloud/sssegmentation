'''ocrnet_hrnetv2w48_voc'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'voc',
    'rootdir': os.path.join(os.getcwd(), 'VOCdevkit/VOC2012'),
})
DATASET_CFG['train']['set'] = 'trainaug'
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update({
    'max_epochs': 60,
})
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify segmentor config
SEGMENTOR_CFG = SEGMENTOR_CFG.copy()
SEGMENTOR_CFG.update({
    'num_classes': 21,
    'backbone': {
        'type': 'hrnetv2_w48',
        'series': 'hrnet',
        'pretrained': True,
        'selected_indices': (0, 0),
    },
    'auxiliary': {
        'in_channels': sum([48, 96, 192, 384]),
        'out_channels': 512,
        'dropout': 0,
    },
    'bottleneck': {
        'in_channels': sum([48, 96, 192, 384]),
        'out_channels': 512,
    },
})
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'ocrnet_hrnetv2w48_voc'
COMMON_CFG['logfilepath'] = 'ocrnet_hrnetv2w48_voc/ocrnet_hrnetv2w48_voc.log'
COMMON_CFG['resultsavepath'] = 'ocrnet_hrnetv2w48_voc/ocrnet_hrnetv2w48_voc_results.pkl'