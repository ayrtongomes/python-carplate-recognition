from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('placa.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
filename = 'placaConv.png'
image = thresh1
cv2.imwrite(filename, image)
