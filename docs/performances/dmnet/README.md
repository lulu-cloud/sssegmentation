# Introduction
```
@InProceedings{He_2019_ICCV,
    author = {He, Junjun and Deng, Zhongying and Qiao, Yu},
    title = {Dynamic Multi-Scale Filters for Semantic Segmentation},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month = {October},
    year = {2019}
}
All the reported models here are available at https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA (code is s757).
```


# Results

## PASCAL VOC
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.38% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_voc_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 76.70% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_voc_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 79.15% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_voc_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 77.76% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_voc_train.log) |

## ADE20k
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.54% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_ade20k_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 41.43% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_ade20k_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 45.53% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_ade20k_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 43.53% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_ade20k_train.log) |

## CityScapes
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.17% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os8_cityscapes_train.log) |
| R-50-D16  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.43% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet50os16_cityscapes_train.log) |
| R-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 79.90% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os8_cityscapes_train.log) |
| R-101-D16 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 78.09% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_dmnet/dmnet_resnet101os16_cityscapes_train.log) |