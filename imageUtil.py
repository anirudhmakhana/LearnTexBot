import numpy as np
import cv2 as cv2

def imageUtil(input_image):
  im = cv2.imread(input_image)
  im[np.where((im == [0,0,0]).all(axis = 2))] = [255, 255, 255]

  cv2.imwrite('./out.png', im)


