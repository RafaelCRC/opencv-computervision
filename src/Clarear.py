import sys
import numpy as np
import cv2 as cv

# Insert 3 parameters: Image path, Index of brightness, random to darken the image
# Insert 2 parameters: Image path, Index of brightness to lighten the image

def main(argv):

    window_name = ('Prewitt - Simple Edge Detector')

    if len(argv) < 2:
        print('Not enough parameters')
        print('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)
    brightness = int(argv[1])
    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    Intensity_Matrix = np.ones(src.shape, dtype = "uint8") * brightness

    b_img = cv.add(src, Intensity_Matrix)
    if (len(sys.argv) > 3):
        b_img = cv.subtract(src, Intensity_Matrix)
    
    

    cv.imshow("brightened img", b_img)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
