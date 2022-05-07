
import sys
import numpy as np
import cv2 as cv

# Insert 3 parameters: Image path, Index of brightness, random to darken the image
# Insert 2 parameters: Image path, Index of brightness to lighten the image

def main(argv):

    window_name_origin = ('Brightness Altered Image')
    window_name = ('Histogram Equalization')

    if len(argv) < 2:
        print('Not enough parameters')
        print('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)
    # Load the brightness setting
    brightness = int(argv[1])
    # Check if image is loaded fine
    if src is None:
        print('Error opening image: ' + argv[0])
        return -1

    # Brightness setting on first image
    Intensity_Matrix = np.ones(src.shape, dtype = "uint8") * brightness
    b_img = cv.add(src, Intensity_Matrix)

    if (len(sys.argv) > 3):
        b_img = cv.subtract(src, Intensity_Matrix)

    cv.imshow(window_name_origin, b_img)

    h_img = b_img

    h_img = np.round(b_img, 0)
    h_img = np.minimum(b_img, 255)
    h_img = np.maximum(b_img, 0)
    h_img = b_img.astype('uint8')

    # Histogram Equalization
    height = h_img.shape[0]
    width = h_img.shape[1]
    hist = np.zeros([256], np.int32)

    # Finding histogram
    for i in range(0, height):
        for j in range(0, width):
            hist[h_img[i, j]] += 1

    # Applying Histogram Equalization
    pdf = hist / hist.sum()

    cdf = np.zeros([256], float)

    for i in range(0, 256):
        for j in range(0, i+1):
            cdf[i] += pdf[j]

    cdf = np.zeros(256, float)
    cdf[0] = pdf[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + pdf[i]

    cdf_eq = np.round(cdf * 255, 0)

    imgEql = np.zeros((height, width))

    # Re-map values into image
    for i in range(0, height):
        for j in range(0, width):
            r = h_img[i, j]
            s = cdf_eq[r] 
            imgEql[i, j] = s

        cv.imshow(window_name, h_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        return 0


if __name__ == "__main__":
    main(sys.argv[1:])
