'''define the config file for ade20k and Swin-B'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'ade20k',
    'rootdir': os.path.join(os.getcwd(), 'ADE20k'),
})
DATASET_CFG['train']['aug_opts'] = [
    ('Resize', {'output_size': (2048, 640), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
    ('RandomCrop', {'crop_size': (640, 640), 'one_category_max_ratio': 0.75}),
    ('RandomFlip', {'flip_prob': 0.5}),
    ('PhotoMetricDistortion', {}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
    ('Padding', {'output_size': (640, 640), 'data_type': 'tensor'}),
]
DATASET_CFG['test']['aug_opts'] = [
    ('Resize', {'output_size': (2048, 640), 'keep_ratio': True, 'scale_range': None}),
    ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
    ('ToTensor', {}),
]
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update(
    {
        'type': 'adamw',
        'adamw': {
            'learning_rate': 0.00006,
            'betas': (0.9, 0.999),
            'weight_decay': 0.01,
            'min_lr': 0.0,
        },
        'max_epochs': 130,
        'params_rules': {'backbone_net_zerowd': (1.0, 0.0), 'others': (1.0, 1.0)},
        'policy': {
            'type': 'poly',
            'opts': {'power': 1.0, 'max_iters': None, 'num_iters': None, 'num_epochs': None},
            'warmup': {'type': 'linear', 'ratio': 1e-6, 'iters': 1500}
        },
    }
)
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify model config
MODEL_CFG = MODEL_CFG.copy()
MODEL_CFG.update(
    {
        'num_classes': 150,
        'backbone': {
            'type': 'swin_base_patch4_window12_384_22k',
            'series': 'swin',
            'pretrained': True,
            'selected_indices': (0, 1, 2, 3),
            'norm_cfg': {'type': 'layernorm', 'opts': {}},
        },
        'ppm': {
            'in_channels': 1024,
            'out_channels': 512,
            'pool_scales': [1, 2, 3, 6],
        },
        'lateral': {
            'in_channels_list': [128, 256, 512],
            'out_channels': 512,
        },
        'fpn': {
            'in_channels_list': [512, 512, 512],
            'out_channels': 512,
        },
    }
)
MODEL_CFG['decoder']['predictor']['in_channels'] = 1024
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['train'].update(
    {
        'backupdir': 'maskformer_swinbase_ade20k_train',
        'logfilepath': 'maskformer_swinbase_ade20k_train/train.log',
    }
)
COMMON_CFG['test'].update(
    {
        'backupdir': 'maskformer_swinbase_ade20k_test',
        'logfilepath': 'maskformer_swinbase_ade20k_test/test.log',
        'resultsavepath': 'maskformer_swinbase_ade20k_test/maskformer_swinbase_ade20k_results.pkl'
    }
)