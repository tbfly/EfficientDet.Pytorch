from .voc0712 import VOCDetection, VOC_CLASSES
from .coco import COCODetection, COCO_CLASSES
from .augmentation import get_augumentation, detection_collate, Resizer, Normalizer, Augmenter, collater
from .cocov2 import CocoDataset