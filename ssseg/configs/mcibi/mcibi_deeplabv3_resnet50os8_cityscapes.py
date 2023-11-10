'''mcibi_deeplabv3_resnet50os8_cityscapes'''
import copy
from .base_cfg import SEGMENTOR_CFG
from .._base_ import DATASET_CFG_CITYSCAPES_512x1024, DATALOADER_CFG_BS16


# deepcopy
SEGMENTOR_CFG = copy.deepcopy(SEGMENTOR_CFG)
# modify dataset config
SEGMENTOR_CFG['dataset'] = DATASET_CFG_CITYSCAPES_512x1024.copy()
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = DATALOADER_CFG_BS16.copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 440
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 19
SEGMENTOR_CFG['backbone'] = {
    'type': 'ResNet', 'depth': 50, 'structure_type': 'resnet50conv3x3stem',
    'pretrained': True, 'outstride': 8, 'use_conv3x3_stem': True, 'selected_indices': (0, 1, 2, 3),
}
SEGMENTOR_CFG['head']['use_loss'] = False
SEGMENTOR_CFG['head']['update_cfg']['momentum_cfg']['base_lr'] = 0.01 * 0.9
SEGMENTOR_CFG['work_dir'] = 'mcibi_deeplabv3_resnet50os8_cityscapes'
SEGMENTOR_CFG['logfilepath'] = 'mcibi_deeplabv3_resnet50os8_cityscapes/mcibi_deeplabv3_resnet50os8_cityscapes.log'
SEGMENTOR_CFG['resultsavepath'] = 'mcibi_deeplabv3_resnet50os8_cityscapes/mcibi_deeplabv3_resnet50os8_cityscapes_results.pkl'