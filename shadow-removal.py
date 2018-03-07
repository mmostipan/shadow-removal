import numpy as np
import cv2


# read an original image
or_img = cv2.imread('shadow.jpg')

# convert the RGB image to a LAB image
lab_img = cv2.cvtColor(or_img, cv2.COLOR_RGB2LAB)

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


# the pixels with a value in L ≤ (mean (L) – standard deviation (L)/3)
def l_shadow_pixels_classifier():
    print("ss")


# the pixels with lower values in both L and B planes
def lb_shadow_pixels_classifier():
    print("dd")


# if mean(A) + mean(B) ≤ 256, then classify...
if a_mean_value + b_mean_value <= 256:
    l_shadow_pixels_classifier()

else:
    lb_shadow_pixels_classifier()


# show both images
cv2.imshow("image", lab_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





