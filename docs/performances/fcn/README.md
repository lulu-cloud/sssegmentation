# Introduction
```
@inproceedings{long2015fully,
    title={Fully convolutional networks for semantic segmentation},
    author={Long, Jonathan and Shelhamer, Evan and Darrell, Trevor},
    booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
    pages={3431--3440},
    year={2015}
}
All the reported models here are available at https://pan.baidu.com/s/1gD-NJJWOtaHCtB0qHE79rA (code is s757).
```


# Results

## PASCAL VOC
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 67.80% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_voc_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 66.58% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_voc_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 70.59% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_voc_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/60  | trainaug/val    | 69.39% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_voc_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_voc_train.log) |

## ADE20k
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 36.96% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_ade20k_train.log) |
| R-50-D16  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 36.50% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_ade20k_train.log) |
| R-101-D8  | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 41.22% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_ade20k_train.log) |
| R-101-D16 | 512x512    | LR/POLICY/BS/EPOCH: 0.01/poly/16/130 | train/val       | 40.15% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_ade20k_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_ade20k_train.log) |

## CityScapes
| Backbone  | Crop Size  | Schedule                             | Train/Eval Set  | mIoU   | Download                 |
| :-:       | :-:        | :-:                                  | :-:             | :-:    | :-:                      |
| R-50-D8   | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 75.16% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os8_cityscapes_train.log) |
| R-50-D16  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 73.94% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet50os16_cityscapes_train.log) |
| R-101-D8  | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 76.31% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os8_cityscapes_train.log) |
| R-101-D16 | 512x1024   | LR/POLICY/BS/EPOCH: 0.01/poly/8/220  | train/val       | 75.36% | [model](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_cityscapes_train.pth) &#124; [log](https://github.com/SegmentationBLWX/modelstore/releases/download/ssseg_fcn/fcn_resnet101os16_cityscapes_train.log) |