'''deeplabv3plus_mobilenetv2os8_voc'''
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
        'type': 'mobilenetv2',
        'series': 'mobilenet',
        'pretrained': True,
        'outstride': 8,
        'selected_indices': (0, 1, 2, 3),
    },
    'aspp': {
        'in_channels': 320,
        'out_channels': 512,
        'dilations': [1, 12, 24, 36],
    },
    'shortcut': {
        'in_channels': 24,
        'out_channels': 48,
    },
    'auxiliary': {
        'in_channels': 96,
        'out_channels': 512,
        'dropout': 0.1,
    },
})
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'deeplabv3plus_mobilenetv2os8_voc'
COMMON_CFG['logfilepath'] = 'deeplabv3plus_mobilenetv2os8_voc/deeplabv3plus_mobilenetv2os8_voc.log'
COMMON_CFG['resultsavepath'] = 'deeplabv3plus_mobilenetv2os8_voc/deeplabv3plus_mobilenetv2os8_voc_results.pkl'