from Polygons.Polygons import Polygon,plt,rndangle,Circumcircle
from Polygons.utils import cropImage,splitQuad

import math,copy
import random
import cv2
import string
import os
import PIL.Image as IMG
import matplotlib.path as mpath
import matplotlib.patches as mpatches

sides = [0,0,2,4] 
XX = [0,10,15,20] 
YY = [10,15,0,20] 

polys = []

plt.figure()
temp = None

for i in range(len(sides)):
    # size = max(random.random()+0.5,0.3+i)* random.choice([70,100])
    size = (i+1)**2 * 100
    # print size
    temp = Polygon(no_of_sides=sides[i],isRegular=False)
    temp.circumcircle = Circumcircle(size,XX[i],YY[i])
    temp.makeShape()
    temp.drawPolygon()
    polys.append(temp)

plt.axis('image')
plt.axis('off')
# plt.show()
plt.savefig('./fold1.png',transparent=True)

# save a flipped version 
os.system('convert fold1.png -flop flipfold1.png')

one = IMG.open('fold1.png').convert('RGBA')
two = IMG.open('flipfold1.png').convert('RGBA')

IMG.alpha_composite(one, two).save("merge.png")

img = cv2.imread('./merge.png',0)
print img.shape

height, width = img.shape
# gives transparent image
os.system('convert fold1.png -strokewidth 1 -fill none -stroke black -draw \"stroke-dasharray 5 3 line '+str(width/2)+',0 '+str(width/2)+','+str(height)+'\" draw_fold.png')
os.system('convert merge.png -strokewidth 1 -fill none -stroke black -draw \"stroke-dasharray 5 3 line '+str(width/2)+',0 '+str(width/2)+','+str(height)+'\" draw_merge.png')
# os.system('convert draw_merge.png  -fill white -draw "rectangle 0,0 '+str(width/2)+','+str(height)+'" draw_final.png')
os.system('convert draw_merge.png  -fill white -draw "rectangle 0,0 '+str(width)+','+str(height)+'" draw_final.png')


# adds white bg
os.system('convert -flatten draw_fold.png draw_fold.png') # question
os.system('convert -flatten draw_merge.png draw_merge.png') # intermediate output
os.system('convert -flatten draw_final.png draw_final.png') # answer


# distractors
for j in range(3):
    
    plt.figure()    
    # additional transformation
    for temp in polys:                
        
        if random.random() <= 0.5:
            temp.flip(how=random.choice(['vert','hori']))
        else:
            temp.rotate(random.choice([-1,+1]) * random.choice([math.pi/4,math.pi/2]))
        temp.drawPolygon()

    plt.axis('image')
    plt.axis('off')
    # plt.show()

    # same base image
    plt.savefig('./fold1.png',transparent=True)

    # save a flipped version 
    os.system('convert fold1.png -flop flipfold1.png')

    one = IMG.open('fold1.png').convert('RGBA')
    two = IMG.open('flipfold1.png').convert('RGBA')

    IMG.alpha_composite(one, two).save("merge.png")

    img = cv2.imread('./merge.png',0)
    print img.shape

    height, width = img.shape
    os.system('convert fold1.png -strokewidth 1 -fill none -stroke black -draw \"stroke-dasharray 5 3 line '+str(width/2)+',0 '+str(width/2)+','+str(height)+'\" draw_fold.png')
    os.system('convert merge.png -strokewidth 1 -fill none -stroke black -draw \"stroke-dasharray 5 3 line '+str(width/2)+',0 '+str(width/2)+','+str(height)+'\" draw_merge.png')
    os.system('convert draw_merge.png  -fill white -draw "rectangle 0,0 '+str(width/2)+','+str(height)+'" draw_final.png')

    os.system('convert -flatten draw_fold.png draw_fold.png') # base distractor
    os.system('convert -flatten draw_merge.png draw_merge'+str(j)+'.png') # intermediate distractor output
    os.system('convert -flatten draw_final.png draw_final'+str(j)+'.png') # final transformed distractor - folded

#################GENERATE DISTRACTORS
## We rotate by 45/90
## We interchange Circumcircle 



