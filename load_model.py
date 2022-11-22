import mmcv
from mmcv.runner import load_checkpoint
from mmdet.models import build_detector


def load_MMDmodel():
    config = 'mmdetection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'
    checkpoint = 'mmdetection/checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
    device='cuda:0'
    config = mmcv.Config.fromfile(config)
    config.model.pretrained = None
    model = build_detector(config.model)
    checkpoint = load_checkpoint(model, checkpoint, map_location=device)
    model.CLASSES = checkpoint['meta']['CLASSES']
    model.cfg = config
    model.to(device)
    model.eval()
    return model


if __name__ == '__main__':
    load_MMDmodel()
