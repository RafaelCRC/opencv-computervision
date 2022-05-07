import numpy as np
import cv2

path = "mergulhador.jpg"
imgSrc = cv2.imread(path,0)
img = imgSrc

window_name_src = ('Src Image')
window_name = ('Histogram Equalization')

cv2.imshow(window_name_src,imgSrc)

a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

# Finding histogram
for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1

# Applying Histogram Equalization
tmp = 1.0/(height*width)
b = np.zeros((256,),dtype=np.float16)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp;
    b[i] = round(b[i] * 255);

b=b.astype(np.uint8)

# Re-map values into image
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]


cv2.imshow(window_name,img)
cv2.waitKey(0)
cv2.destroyAllWindows()