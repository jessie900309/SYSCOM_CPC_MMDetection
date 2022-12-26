from mmdet.apis import inference_detector
import mmcv
import cv2
from os import listdir, system
from os.path import basename, isfile


def ffmpegMP4(inputMP4):
    system('ffmpeg -i "syscom_video/{}" "syscom_convert_video/{}"'.format(inputMP4, inputMP4))


def convertMP4(inputMP4, model):
    if isfile(inputMP4):
        input_video = inputMP4
        video = mmcv.VideoReader(input_video)
        img_index = 0
        input_video_name = basename(input_video)[:-4]
        for frame in video:
            result = inference_detector(model, frame)
            save_img = 'syscom_video_frame/{}/result{}.jpg'.format(input_video_name, img_index)
            model.show_result(frame, result, score_thr=0.3, font_size=0, thickness=0, out_file=save_img)
            img_index += 1
            if img_index%10 == 0:
                print("...result{}.jpg".format(img_index))
    else:
        print("{} is not a file!".format(inputMP4))


def convertJPGtoMP4(inputMP4):
    input_video = inputMP4
    input_video_name = basename(input_video)[:-4]
    input_video_frame_dir = 'syscom_video_frame/' + input_video_name
    # get all image
    len_of_image_list = len(listdir(input_video_frame_dir))
    print("len of image list = ", len_of_image_list)
    if len_of_image_list > 0:
        # get image W/H
        img = cv2.imread('{}/result0.jpg'.format(input_video_frame_dir))
        size = (img.shape[1], img.shape[0])
        print("size = ", size)
        # get FPS
        video = cv2.VideoCapture(input_video)
        fps = video.get(cv2.CAP_PROP_FPS)
        print("fps = ", fps)
        # write MP4
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        videowrite = cv2.VideoWriter('output_video/result{}.mp4'.format(input_video_name), fourcc, fps, size)
        for index in range(len_of_image_list):
            img_path = "{}/result{}.jpg".format(input_video_frame_dir, str(index))
            img = cv2.imread(img_path)
            videowrite.write(img)
        # output
        videowrite.release()
        print('output video : output_video/result{}.mp4'.format(input_video_name))
    else:
        print('img is None')


if __name__ == '__main__':
    print("nothingOuO")
