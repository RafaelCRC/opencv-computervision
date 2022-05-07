import sys
import cv2 as cv
import numpy as np

def main(argv):
    window_name = ('TresholdBinarySegmentation')

    if len(argv) < 1:
        print('Not enough parameters')
        print('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1

    src = cv.imread(argv[0], cv.IMREAD_GRAYSCALE) #grayscale

    width, height = np.shape(src) #altura e largura

    threshold = (src.max() + src.min()) / 2 #limiar
    initialTreshold = threshold 
    
    while abs(threshold - initialTreshold) != 0:
        R1 = np.array([])
        R2 = np.array([])
        for i in range(width):
            for y in range(height):
                if src[i, y] >= threshold:
                    R1 = np.append(R1, src[i, y])
                else:
                    R2 = np.append(R2, src[i, y])
        
        threshold = (np.mean(R1) + np.mean(R1)) / 2

    for i in range(width):
            for y in range(height):
                if src[i, y] >= threshold:
                    src[i, y] = 255
                else:
                    src[i, y] = 0

    cv.imshow(window_name, src)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv[1:])