from Polygons.Polygons import Polygon,plt,rndangle,Circumcircle
from Polygons.utils import cropImage,splitQuad

import math,copy
import random
import cv2



# plt.gca().add_patch(polygon)



gridSize = 25
radius = 10


startX = 0
startY = 0

def shift_polys(polys,pos_by=1,hatch_by=1):
    tmep_polys = copy.deepcopy(polys)

def draw_polygon_grid(poly,index):
    # The incoming index is 1 to 9
    index -=1 
    X = index / 3
    Y = index % 3
    # print(index,i,j)
    poly.circumcircle = Circumcircle(radius, startX + Y*gridSize, startY - X*gridSize)
    poly.makeShape()     




plt.figure()
# This is to get a bordor so that while croping, we do not crop the white 
# spaces we want to show.

plt.gca().add_patch(
    plt.Rectangle(
        (-gridSize/2,-gridSize*3+gridSize/2 ),   # (x,y)
        gridSize*3,          # width
        gridSize*3,          # height
        fill=None,
        # edgecolor='black'
    )
)

# plt.gca().add_patch(
#     plt.Rectangle(
#         (-gridSize/2+gridSize*,-gridSize*1+gridSize/2 ),   # (x,y)
#         gridSize,          # width
#         gridSize,          # height
#         # fill=None,
#         # edgecolor='black'
#     )
# )



# plt.gca().add_patch(
#     plt.Rectangle(
#         (-gridSize/2,-gridSize*3+gridSize/2 ),   # (x,y)
#         gridSize,          # width
#         gridSize,          # height
#         fill=None,
#         # edgecolor='black'
#     )
# )

# draw boxes grid 
for i in range(3):
    for j in range(3):
        plt.gca().add_patch(
            plt.Rectangle(
                (-gridSize/2+gridSize*i,-gridSize*(j+1)+gridSize/2 ),   # (x,y)
                gridSize,          # width
                gridSize,          # height
                fill=None,
                edgecolor='blue'
                )
    )






polys = []
XX=0

rank = range(1,10)
random.shuffle(rank)

# for i in range(1,10):
#     temp = Polygon(no_of_sides=XX+3,isRegular=False,hatch='random')
#     draw_polygon_grid(temp,i)
#     temp.drawPolygon()
#     polys.append(temp)
#     XX+=1

for i in rank:
    temp = Polygon(no_of_sides=int(random.random()*6),isRegular=False,hatch='random')
    draw_polygon_grid(temp,i)
    temp.drawPolygon()
    polys.append(temp)
    XX+=1


# for i in range(3):
#     for j in range(3):
#         temp = Polygon(no_of_sides=XX+3,isRegular=False,hatch='random')
#         temp.circumcircle = Circumcircle(radius, startX + j*gridSize, startY - i*gridSize)
#         temp.makeShape()
#         polys.append(temp)
#         # temp.circumcircle.radius = radius
#         # temp.circumcircle.x = startX + j*gridSize
#         # temp.circumcircle.y = startY + i*gridSize
#         # temp.gen_points()
#         # print temp.points
#         temp.drawPolygon()
#         XX+=1

# print len(polys)
plt.axis('off') 

plt.axis('image')
plt.savefig('./grid.png')

img = cv2.imread('./grid.png',0)
img = cropImage(img)    
cv2.imwrite('./grid.png',img)

for _ in range(8):
    plt.figure()
    plt.gca().add_patch(
        plt.Rectangle(
            (-gridSize/2,-gridSize*3+gridSize/2 ),   # (x,y)
            gridSize*3,          # width
            gridSize*3,          # height
            fill=None,
            # edgecolor='black'
        )
    )

    # draw boxes grid 
    for i in range(3):
        for j in range(3):
            plt.gca().add_patch(
                plt.Rectangle(
                    (-gridSize/2+gridSize*i,-gridSize*(j+1)+gridSize/2 ),   # (x,y)
                    gridSize,          # width
                    gridSize,          # height
                    fill=None,
                    edgecolor='blue'
                    )
        )


    # shift polygons by one position
    temp_circumcircle = polys[0].circumcircle
    for i in range(len(polys)-1):
        polys[i].circumcircle = polys[i+1].circumcircle
        # polys[i].rotate(math.pi/2)
    polys[len(polys)-1].circumcircle = temp_circumcircle


    for i in range(len(polys)):
        # polys[i].circumcircle =temp_polys[i].circumcircle
        # polys[i].hatch = '*' if i%2 == 0 else '\\'
        polys[i].gen_points()
        polys[i].drawPolygon()



      
    plt.axis('off') 

    plt.axis('image')
    plt.savefig('./grid'+str(_)+'.png')

    img = cv2.imread('./grid'+str(_)+'.png',0)
    img = cropImage(img)    
    cv2.imwrite('./grid'+str(_)+'.png',img)

# plt.figure()
# plt.gca().add_patch(
#     plt.Rectangle(
#         (-gridSize/2,-gridSize*3+gridSize/2 ),   # (x,y)
#         gridSize*3,          # width
#         gridSize*3,          # height
#         fill=None,
#         # edgecolor='black'
#     )
# )

# # shift polygons by one position
# temp_circumcircle = polys[0].circumcircle
# for i in range(len(polys)-1):
#     polys[i].circumcircle = polys[i+1].circumcircle
# polys[len(polys)-1].circumcircle = temp_circumcircle


# for i in range(len(polys)):
#     # polys[i].circumcircle =temp_polys[i].circumcircle
#     # polys[i].hatch = '*' if i%2 == 0 else '\\'
#     polys[i].gen_points()
#     polys[i].drawPolygon()

# plt.axis('off') 
# plt.axis('image')
# plt.savefig('./grid3.png')

# img = cv2.imread('./grid3.png',0)
# img = cropImage(img)    
# cv2.imwrite('./grid3.png',img)


