'''base config for ConvNeXt'''
# config for dataset
DATASET_CFG = {
    'type': '',
    'rootdir': '',
    'train': {
        'set': 'train',
        'aug_opts': [
            ('Resize', {'output_size': (2048, 512), 'keep_ratio': True, 'scale_range': (0.5, 2.0)}),
            ('RandomCrop', {'crop_size': (512, 512), 'one_category_max_ratio': 0.75}),
            ('RandomFlip', {'flip_prob': 0.5}),
            ('PhotoMetricDistortion', {}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
            ('Padding', {'output_size': (512, 512), 'data_type': 'tensor'}),
        ],
    },
    'test': {
        'set': 'val',
        'aug_opts': [
            ('Resize', {'output_size': (2048, 512), 'keep_ratio': True, 'scale_range': None}),
            ('Normalize', {'mean': [123.675, 116.28, 103.53], 'std': [58.395, 57.12, 57.375]}),
            ('ToTensor', {}),
        ],
    }
}
# config for dataloader
DATALOADER_CFG = {
    'train': {
        'batch_size': 16, 'num_workers': 16, 'shuffle': True, 'pin_memory': True, 'drop_last': True,
    },
    'test': {
        'batch_size': 1, 'num_workers': 16, 'shuffle': False, 'pin_memory': True, 'drop_last': False,
    }
}
# config for optimizer
OPTIMIZER_CFG = {
    'type': 'adamw',
    'lr': 0.0001,
    'betas': (0.9, 0.999),
    'weight_decay': 0.05,
    'params_rules': {'type': 'layerdecay', 'decay_rate': 0.9, 'decay_type': 'stage_wise', 'num_layers': 12},
}
# config for scheduler
SCHEDULER_CFG = {
    'type': 'poly',
    'max_epochs': 0,
    'power': 0.9,
}
# config for losses
LOSSES_CFG = {
    'loss_aux': {
        'celoss': {'scale_factor': 0.4, 'ignore_index': 255, 'reduction': 'mean'}
    },
    'loss_cls': {
        'celoss': {'scale_factor': 1.0, 'ignore_index': 255, 'reduction': 'mean'}
    },
}
# config for segmentor
SEGMENTOR_CFG = {
    'type': 'upernet',
    'num_classes': -1,
    'benchmark': True,
    'align_corners': False,
    'backend': 'nccl',
    'norm_cfg': {'type': 'syncbatchnorm'},
    'act_cfg': {'type': 'relu', 'inplace': True},
    'backbone': {
        'type': 'convnext_base',
        'series': 'convnext',
        'arch': 'base',
        'pretrained': True,
        'drop_path_rate': 0.4,
        'layer_scale_init_value': 1.0,
        'gap_before_final_norm': False,
        'selected_indices': (0, 1, 2, 3),
        'norm_cfg': {'type': 'layernorm2d', 'eps': 1e-6},
    },
    'head': {
        'in_channels_list': [128, 256, 512, 1024],
        'feats_channels': 512,
        'pool_scales': [1, 2, 3, 6],
        'dropout': 0.1,
    },
    'auxiliary': {
        'in_channels': 512,
        'out_channels': 512,
        'dropout': 0.1,
    }
}
# config for inference
INFERENCE_CFG = {
    'mode': 'slide',
    'opts': {'cropsize': (512, 512), 'stride': (341, 341)}, 
    'tricks': {
        'multiscale': [1],
        'flip': False,
        'use_probs_before_resize': False
    }
}
# config for common
COMMON_CFG = {
    'work_dir': 'ckpts',
    'logfilepath': '',
    'log_interval_iterations': 50,
    'eval_interval_epochs': 10,
    'save_interval_epochs': 1,
    'resultsavepath': '',
}