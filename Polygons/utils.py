"""
Methods related to processing the complete image 
as a whole 
"""
# http://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
import cv2,numpy as np

"""
Takes cv2 image object. Returns the cropped image object.
"""
def cropImage(img):
    # Invert colors so that opencv can find bounding rectangle
    img = invertColors(img)
    # Find bounding rectangles
    x,y,w,h = cv2.boundingRect(img)

    # Crop image
    crop_img = img[y:y+h, x:x+w]

    # Invert colors to restore the original image 
    crop_img = invertColors(crop_img)

    return crop_img
    
"""
Turns black over white to white over black
and vice-versa
"""
def invertColors(img):
    img = cv2.bitwise_not(img)
    return img
    # for i in range(len(img)):
    #     for j in range(len(img[i])):
    #         img[i][j] = 0 if img[i][j] == 255 else 255    

"""
Returns true if img is a square image
"""
def isSquare(img):
    return img.shape[0] == img.shape[1]

"""
Splits given square image into a quadrant and the rest of the image
returns quad,rest_og_the_image
"""
def splitQuad(img,quad_number=0):
    # 0,1,2,4 => first_quad,second_quad,third_quad,fourth_quad 
    quad_number = quad_number % 4
    width,height = img.shape
    tmp_img = np.copy(img)

    if quad_number == 0:
        tmp_img[0:height/2,width/2:width] = 255
        # cv2.rectangle(tmp_img, (width/2,0),(width,height/2),0)
        return img[0:height/2,width/2:width],tmp_img
    elif quad_number == 1:
        tmp_img[0:height/2,0:width/2] = 255
        return img[0:height/2,0:width/2],tmp_img
    elif quad_number == 2 :
        tmp_img[height/2:height,0:width/2] = 255
        return img[height/2:height,0:width/2],tmp_img
    else:
        tmp_img[height/2:height,width/2:width] = 255
        return img[height/2:height,width/2:width],tmp_img
    


