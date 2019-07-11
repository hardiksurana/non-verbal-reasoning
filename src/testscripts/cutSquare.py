import sys
sys.path.insert(0, '/Users/hardik/Desktop/projects/turtle/')
# sys.path.insert(0, '')
import cv2 
# from turtle.Polygons.utils import isSquare
from Polygons.utils import isSquare
# Relative from the base package
# img = cv2.imread('./tmp/square.png',0)
img = cv2.imread('./tmp/dice_1.png',0)
# img = img[]

# print(img.shape)
print(isSquare(img))
width = img.shape[1]
height = img.shape[0]

first_quad = img[0:height/2,width/2:width]
cv2.imwrite('./tmp/1square.png',first_quad)
second_quad = img[0:height/2,0:width/2]
cv2.imwrite('./tmp/2square.png',second_quad)
third_quad = img[height/2:height,0:width/2]
cv2.imwrite('./tmp/3square.png',third_quad)
fourth_quad = img[height/2:height,width/2:width]
cv2.imwrite('./tmp/4square.png',fourth_quad)

# if isSquare(img):
#     print("Image is square")