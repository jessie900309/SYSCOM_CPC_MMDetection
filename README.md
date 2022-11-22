# SYSCOM_CPC_MMDetection

###### tags: `SYSCOM` `GitHub`



## Install MMDetection

1. 確定電腦的GPU是NVIDIA的 (會用到CUDA)
2. 如果是打包專案的話，可以直接試試[**Run**](https://hackmd.io/Beum6GgLQ9urQ7zI3EeP4g#Run)
3. 如果出現套件未安裝的錯誤訊息，依序執行以下指令
    1. **安裝 PyTorch**
    `pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html`
    2. **安裝 mmcv-full**
    `pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html`
    3. <font color=red>**(!!!接下來的指令，如果是直接打包專案的話不用跑!!!)**</font>
        安裝 MMDetection
        `rm -rf mmdetection`
        (Windows CMD 沒有 `rm` 需要手動刪除 `mmdetection` 資料夾)
        `git clone https://github.com/open-mmlab/mmdetection.git`
        (電腦如果沒有Git可以直接到[官方](https://github.com/open-mmlab/mmdetection)下載完整專案再解壓縮)
        `cd mmdetection`
        `pip install -e .`
        `mkdir checkpoints`
        `wget -c https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth \
          -O checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth`
          (Windows CMD 沒有 `wget` 需要手動下載官方提供的[模型](https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth)，並在 `mmdetection` 資料夾下創建名為 `checkpoints` 的資料夾，並把下載好的模型丟進去)


## Run

1. 把要辨識的影片放到 `syscom_video` 目錄
    <img width='500px' src='https://i.imgur.com/gpNh3Th.png'/>
2. 執行 `main.py`
    <img width='500px' src='https://i.imgur.com/Z3lTb88.png'/>
    過程中出現UserWarning、Warning，還有下面那一堆都是正常的
    <img width='500px' src='https://i.imgur.com/Kdy99xB.png'/>
    等到出現 `output video : XXXXXX.mp4` 表示該影片轉換完成
    <img width='500px' src='https://i.imgur.com/jPJr1QT.png'/>
3. 辨識完成的影片會在 `output_video` 目錄
    <img width='500px' src='https://i.imgur.com/J4sPxup.png'/>




