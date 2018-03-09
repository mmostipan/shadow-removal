import numpy as np
import cv2


# read an original image
or_img = cv2.imread('shadow.jpg')

rows, columns, channels = or_img.shape

# convert the BGR image to a LAB image
lab_img = cv2.cvtColor(or_img, cv2.COLOR_BGR2LAB)

# channels of the converted image will be split into their individual planes
l, a, b = cv2.split(lab_img)

# get mean value of the pixels in L plane
l_mean_value = np.mean(l)

# get standard deviation of channel in L plane
l_std = np.std(l)

# get mean value of the pixels in A plane
a_mean_value = np.mean(a)

# get mean value of the pixels in B plane
b_mean_value = np.mean(b)

# get standard deviation of channel in B plane
b_std = np.std(b)

# get a const for l to remove the shadow, (114.6 is mean value of the pixels in shadow)
const_l = (l_mean_value + l_std) - 114.6

# get a const for b to remove the shadow, (131.7 is mean value of the pixels in shadow)
const_b = (b_mean_value + b_std ) - 131.7


# the pixels with a value in L ≤ (mean (L) – standard deviation (L)/3)
def l_shadow_pixels_classifier():
    print("ss")


# the pixels with lower values in both L and B planes
def lb_shadow_pixels_classifier():
    for i in range(rows):
        for j in range(columns):
            l_px = lab_img[i, j, 0]
            a_px = lab_img[i, j, 1]
            b_px = lab_img[i, j, 2]
            if l_px < l_mean_value - (l_std / 3) and b_px < b_mean_value - (b_std / 3):
                lab_img[i, j] = [l_px + const_l, a_px, b_px + const_b]


# if mean(A) + mean(B) ≤ 256, then classify...
if a_mean_value + b_mean_value <= 256:
    l_shadow_pixels_classifier()

else:
    lb_shadow_pixels_classifier()

mask1 = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)

# show both images
cv2.imshow("image1", or_img)
cv2.imshow("image2", mask1)

cv2.waitKey(0)
cv2.destroyAllWindows()





