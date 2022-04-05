import sys
import numpy as np
import cv2 as cv


def main(argv):

    window_name = ('Prewitt - Simple Edge Detector')
    ddepth = cv.CV_16S

    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    img_neg = 255 - src

    cv.imshow(window_name, img_neg)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
