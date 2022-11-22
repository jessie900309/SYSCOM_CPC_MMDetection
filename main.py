import os
from convert_function import convertMP4, convertJPGtoMP4, ffmpegMP4
from load_model import load_MMDmodel


input_video_dir = 'syscom_video'


def main():
    # load model
    MMDmodel = load_MMDmodel()
    # result
    for input_video in os.listdir(input_video_dir):
        input_video_path = input_video_dir + '/' + input_video
        print("now convert " + input_video_dir + '/' + input_video + '...')
        ffmpegMP4(input_video)
        convertMP4('syscom_convert_video' + '/' + input_video, MMDmodel)
        print("convert image list to video...")
        convertJPGtoMP4(input_video_path, MMDmodel)


if __name__ == '__main__':
    main()
