# -*- coding: utf-8 -*-

import cv2
import os
import glob
import sys

IMAGE_PATH = "./gif"

DESTINATION = "splitted"

def get_frames(path):
    #get list of frame in "path"
    dir_name = "splitted"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    i = 0
    gif = cv2.VideoCapture(path)
    while True:
        print("reading " + path + "...")
        is_success, frame = gif.read()
        if not is_success:
            break

        img_name = path.replace(IMAGE_PATH + "/", "").replace(".gif", "-") + str(i) + ".png"
        img_path = os.path.join(dir_name, img_name)
        print("saving " + img_path)
        cv2.imwrite(img_path, frame)
        i += 1

def main():
    file_list = glob.glob(IMAGE_PATH + "/*.gif")
    for _file in file_list:
        frames = get_frames(_file)

if __name__ == "__main__":
    main()
