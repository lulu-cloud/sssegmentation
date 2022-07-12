'''memorynet_resnet101os8_coco'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'coco',
    'rootdir': os.path.join(os.getcwd(), 'COCO'),
})
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update({
    'max_epochs': 30
})
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify segmentor config
SEGMENTOR_CFG = SEGMENTOR_CFG.copy()
SEGMENTOR_CFG.update({
    'num_classes': 21,
})
SEGMENTOR_CFG['memory']['use_loss'] = False
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'memorynet_resnet101os8_coco'
COMMON_CFG['logfilepath'] = 'memorynet_resnet101os8_coco/memorynet_resnet101os8_coco.log'
COMMON_CFG['resultsavepath'] = 'memorynet_resnet101os8_coco/memorynet_resnet101os8_coco_results.pkl'