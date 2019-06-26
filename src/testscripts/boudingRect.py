
# http://docs.opencv.org/trunk/dd/d49/tutorial_py_contour_features.html
import cv2


def cropImage(img):
    # Invert colors so that opencv can find bounding rectangle
    invertColors(img)
    # Find bounding rectangles
    x,y,w,h = cv2.boundingRect(img)

    # Crop image
    crop_img = img[y:y+h, x:x+w]

    # Invert colors to restore the original image 
    invertColors(crop_img)

    return crop_img

def invertColors(img):
    # Invert colors for cropping
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = 0 if img[i][j] == 255 else 255    




# img = cv2.imread('star.png',0)
# print img
# invertColors(img)
# cv2.imwrite("invert.png", img)
# # invertColors(img)
# # cv2.imwrite("doubleinvert.png", img)

# # Find bounding rectangles
# x,y,w,h = cv2.boundingRect(img)
# print x,y,w,h

# # Crop image
# crop_img = img[y:y+h, x:x+w]


# # invertColors(crop_img)
# # save cropped image
# cv2.imwrite("cropped.png", crop_img)
# invertColors(crop_img)
# cv2.imwrite("invertcropped.png", crop_img)

