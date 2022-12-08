# SYSCOM_CPC_MMDetection

###### tags: `SYSCOM` `GitHub`



:::spoiler Contents
[TOC]
:::



## Install
### Step 1
1. 確定電腦的GPU是NVIDIA的 (會用到CUDA)
2. 下載專案並解壓縮
    <img width='500px' src='https://i.imgur.com/Cwx1AGI.png'/>
### Step 2
1. 安裝 PyTorch
    `pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html` (沒有換行)
2. 安裝 mmcv-full
    `pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html` (沒有換行)
3. 安裝 opencv
    `pip install opencv-python`
    安裝 opencv <font color='red'>不要</font>使用`pip install cv2`或是`pip install opencv`
    如果因為IDE預設按了安裝，請使用`pip uninstall cv2`或是`pip uninstall opencv`解除安裝
### Step 3
* <font color='orange'>**Windows / 電腦沒有Git**</font>
    1. 刪除舊的套件
        手動刪除 mmdetection 資料夾
    2. 安裝 MMDetection 
        直接到官方下載完整專案再解壓縮，並將解壓縮後的檔案放入專案資料夾
        <img width='500px' src='https://i.imgur.com/rWidYK1.png'/>
        <img width='500px' src='https://i.imgur.com/RotUF5G.png'/>
    3. `cd mmdetection`
    4. `pip install -e .`
* <font color='orange'>**Linux**</font>
    1. 刪除舊的套件
        `rm -rf mmdetection`
        執行錯誤 → 手動刪除 mmdetection 資料夾
    2. 安裝 MMDetection 
        `git clone https://github.com/open-mmlab/mmdetection.git`
        執行錯誤 → 電腦如果沒有Git可以直接到官方下載完整專案再解壓縮，並將解壓縮後的檔案放入專案資料夾
    3. `cd mmdetection`
    4. `pip install -e .`
### Step 4
* <font color='orange'>**Windows / 電腦沒有Git**</font>
    1. 建立資料夾
        在上一步驟中的 mmdetection 資料夾中建立名為 `checkpoints` 的資料夾
    2. 下載 [model](https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth)
    3. 把下載好的 model 丟進 checkpoints 資料夾
        <img width='500px' src='https://i.imgur.com/s0U0AwP.png'/>
* <font color='orange'>**Linux**</font>
    1. 建立資料夾
        `mkdir checkpoints`
    2. 下載model
        `wget -c https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth -O checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth` (沒有換行)
        執行錯誤 → 手動下載官方提供的模型，並把下載好的 model 丟進 checkpoints 資料夾
### Step 5
* <font color='orange'>**Windows**</font> (僅Windows電腦需要執行，因為Windows認不得mmdet套件)
    1. 在 mmdetection 資料夾中找到`setup.py`，並用記事本開啟
        將 `extra_compile_args = {'cxx': []}` 
        改為 `extra_compile_args = {'cxx': ["-DMS_WIN64","-MD"]}`
        <img width='500px' src='https://i.imgur.com/Cezd1uD.png'/>
        <img width='500px' src='https://i.imgur.com/6B4G8rr.png'/>
    2. 將 mmdetection 資料夾中的`requirements.txt`內容改為
        ```
        cython
        numpy
        cityscapesscripts
        imagecorruptions
        scipy
        sklearn
        matplotlib
        numpy
        # pycocotools
        six
        terminaltables
        asynctest
        codecov
        flake8
        interrogate
        isort==4.3.21
        # Note: used for kwarray.group_items, this may be ported to mmcv in the future.
        kwarray
        # Note: NO GIT (2022.11.22)
        # -e git+https://github.com/open-mmlab/mmtracking#egg=mmtrack
        # onnx==1.7.0
        onnxruntime>=1.8.0
        protobuf<=3.20.1
        pytest
        ubelt
        xdoctest>=0.10.0
        yapf
        ```
    3. 存檔後關閉檔案
    4. `cd mmdetection` (若CMD已在mmdetection目錄下則不用打這行)
    5. `pip install -r requirements.txt`
### Step 6
1. 安裝 pycocotools 
    `pip install pycocotools`
    <font color='red'>執行成功 → 直接跳至Step 7</font>
    執行錯誤 → 因為原始的pycocotools不支援Windows10，或電腦沒有VS的Build Tools，請繼續執行下列指令
2. 至[Microsoft官網](https://visualstudio.microsoft.com/zh-hant/visual-cpp-build-tools/)下載Build Tools
    <img width='500px' src='https://i.imgur.com/LEo7H1q.png'/>
3. 下載完成後，直接執行該exe檔
4. Microsoft C++ Build Tools安裝完成後，會出現下列畫面
    勾選[使用C++的桌面開發] 在按右下角的[安裝]
    <img width='250px' src='https://i.imgur.com/ebFgY8G.png'/><img width='250px' src='https://i.imgur.com/8LMz8Im.png'/>
5. 安裝完成後重新開機，再回到CMD輸入指令 
    `pip install pycocotools`
6. 檢查是否成功安裝成功，查看列表是否有 pycocotools，如果有的話表示安裝成功
    `pip list`
### Step 7
1. 編譯
    `python setup.py build_ext --inplace`
2. 安裝
    `python setup.py install develop`
3. 檢查是否成功安裝成功，查看列表是否有 mmdet，如果有的話表示安裝成功
    `pip list`
4. 安裝mim安裝工具
    `pip install openmim`
5. 安裝完整mmcv
    `mim install mmcv-full==1.6.0`
6. 檢查是否成功安裝成功，查看列表是否有 mmcv-full，如果有的話表示安裝成功
    `pip list`
### Step 8
1. 確認是否有安裝 ffmpeg 並加入環境變數
    開啟CMD並輸入 ffmpeg -version，如果有裝的話，應該會顯示版本及相關資訊(如左圖);如果沒裝或是沒有將其加入環境變數則會出現錯誤訊息(如右圖)
    <img width='250px' src='https://i.imgur.com/UK8ZUIF.png'/><img width='250px' src='https://i.imgur.com/IAJ5OmW.png'/>
    <font color='red'>執行成功 → 直接跳至Step 9</font>
    執行錯誤 → 因為原始的pycocotools不支援Windows10，或電腦沒有VS的Build Tools，請繼續執行下列指令
2. 如果電腦沒有 ffmpeg，先至[官網](https://ffmpeg.org/download.html)下載符合電腦作業系統ffmpeg (以Windows為例)
    <img width='250px' src='https://i.imgur.com/cEV0O2E.png'/><img width='250px' src='https://i.imgur.com/h1t8riW.png'/>
3. 將解壓縮的資料夾命名為 ffmpeg 並存到本機 (我自己習慣統一放在src資料夾下)
    <img width='500px' src='https://i.imgur.com/EZKMZ8H.png'/>
4. 配置環境變數
    對著[本機]右鍵點擊[內容] ，接下來的步驟請參考下圖數字
    <img width='500px' src='https://i.imgur.com/LQV2FHm.png'/>
5. 最後確認有安裝成功，應該會顯示版本及相關資訊
    `ffmpeg -version`
### Step 9
1. 把要辨識的影片放到 syscom_video 資料夾
    <img width='500px' src='https://i.imgur.com/YwI5Fz2.png'/>



## Run
1. 在專案目錄下開啟CMD
    (或是PowerShell也可以)
    <img width='500px' src='https://i.imgur.com/xIyDUe6.png'/>
2. `py main.py`
    過程中出現UserWarning、Warning都是正常的
    若不是第一次執行，可能會出現下列訊息 : 
    <img width='500px' src='https://i.imgur.com/f5RZGlo.png'/>
    已有相同檔案存在，是否覆寫? [確認覆寫請輸入 y 並按enter繼續執行]
3. 等到出現 `output video : XXXXXX.mp4` 表示該影片轉換完成
    <img width='500px' src='https://i.imgur.com/zR8F4I7.png'/>
4. 辨識完成的影片會在 output_video 資料夾
    <img width='500px' src='https://i.imgur.com/a7sCqEz.png'/>


