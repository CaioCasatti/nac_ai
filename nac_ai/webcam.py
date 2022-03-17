import cv2
import os,sys, os.path
import numpy as np


def image_da_webcam(img):

    img = cv2.imread('circulo.png')

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



    image_lower_hsvBolaAzul = np.array([85, 160, 210])  
    image_upper_hsvBolaAzul = np.array([95, 185, 230])

    mask_hsvBolaAzul = cv2.inRange(img_hsv, image_lower_hsvBolaAzul, image_upper_hsvBolaAzul)

    image_lower_hsvBolaVermelha1 = np.array([0, 110, 110])  
    image_upper_hsvBolaVermelha1 = np.array([10, 240, 240])

    mask_hsvBolaVermelha1 = cv2.inRange(img_hsv, image_lower_hsvBolaVermelha1, image_upper_hsvBolaVermelha1)

    image_lower_hsvBolaVermelha2 = np.array([170, 110, 110])  
    image_upper_hsvBolaVermelha2 = np.array([180, 240, 240])

    mask_hsvBolaVermelha2 = cv2.inRange(img_hsv, image_lower_hsvBolaVermelha2, image_upper_hsvBolaVermelha2)

    mask_hsvBolaVermelha = cv2.bitwise_or(mask_hsvBolaVermelha1, mask_hsvBolaVermelha2)


    mask_hsvTotal = cv2.bitwise_or(mask_hsvBolaVermelha, mask_hsvBolaAzul)

    return mask_hsvTotal

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    
    img = image_da_webcam(frame)


    cv2.imshow("preview", img)

    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()
