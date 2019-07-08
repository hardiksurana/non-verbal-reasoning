from Polygons.Polygons import Polygon, plt, rndangle, Circumcircle
from Polygons.utils import cropImage, splitQuad

import math
import copy
import os
import random
import cv2

gridSize = 25
radius = 10
startX = 0
startY = 0


def shift_polys(polys, pos_by=1, hatch_by=1):
    tmep_polys = copy.deepcopy(polys)


def draw_grid():
    # This is to get a bordor so that while croping, we do not crop the whitespaces we want to show.

    plt.gca().add_patch(
        plt.Rectangle(
            (-gridSize/2, -gridSize*3+gridSize/2),   # (x,y)
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
                    (-gridSize/2+gridSize*i, -gridSize*(j+1)+gridSize/2),   # (x,y)
                    gridSize,          # width
                    gridSize,          # height
                    fill=None,
                    edgecolor='blue'
                )
            )


def draw_polygon_grid(poly, index):
    # The incoming index is 1 to 9
    # Assigngs the figure a appropriate circumcircle
    index -= 1
    X = index / 3
    Y = index % 3
    # print(index,i,j)
    poly.circumcircle = Circumcircle(
        radius, startX + Y*gridSize, startY - X*gridSize)
    poly.makeShape()
    poly.drawPolygon()


if random.random() < 0.5:
    ####################################################################################
    # LOGIC 1
    # Draw polygons and then cyclic rpelacement with
    # some sequence.

    # ---------------------------------------------
    # GENERATE a list of RANDOM FIGURES
    plt.figure()
    draw_grid()
    polys = []
    XX = 0

    a = range(1, 10)
    random.shuffle(a)
    rank = random.choice([a, [a[i] for i in range(int(random.random()*9))]])
    # random.shuffle(rank)

    for i in rank:
        temp = Polygon(no_of_sides=int(random.random()*6),
                       isRegular=False, hatch='random')
        draw_polygon_grid(temp, i)
        # temp.drawPolygon()
        polys.append(temp)
        XX += 1

    # print len(polys)
    plt.axis('off')
    plt.axis('image')
    plt.savefig('./grid.png', dpi=150)
    # ,dpi=150
    img = cv2.imread('./grid.png', 0)
    img = cropImage(img)
    cv2.imwrite('./grid.png', img)
    # ---------------------------------------------

    #################################################

    for _ in range(8):

        plt.figure()
        draw_grid()

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
        plt.savefig('./grid'+str(_)+'.png', dpi=150)

        img = cv2.imread('./grid'+str(_)+'.png', 0)
        img = cropImage(img)
        cv2.imwrite('./grid'+str(_)+'.png', img)

    os.system(
        'montage -mode concatenate -tile 5x1 -border 5 grid.png grid[0-3].png grid_final.png')
    names = ['grid4.png', 'grid5.png', 'grid6.png', 'grid7.png']
    random.shuffle(names)
    os.system('montage -mode concatenate -tile 4x1 -border 5 ' +
              ' '.join(names)+' grid_options.png')

    ##########################################################


else:

    ##################################################################################
    # LOGIC2: transfer the hatch as well
    print("##2")

    # ---------------------------------------------
    # GENERATE a list of RANDOM FIGURES
    plt.figure()
    draw_grid()
    polys = []
    XX = 0

    rank = range(1, 10)
    random.shuffle(rank)

    hatches = ['-', '+', 'x', '\\', '*', 'o', 'O', '.', '/', '|']
    random.shuffle(hatches)

    for i in rank:
        temp = Polygon(no_of_sides=int(random.random()*6)+3,
                       isRegular=False, hatch=hatches[i % 10])
        draw_polygon_grid(temp, i)
        # temp.drawPolygon()
        polys.append(temp)
        # print temp.hatch
        XX += 1

    # print len(polys)
    plt.axis('off')
    plt.axis('image')
    plt.savefig('./grid.png', dpi=150)
    # ,dpi=150
    img = cv2.imread('./grid.png', 0)
    img = cropImage(img)
    cv2.imwrite('./grid.png', img)
    # ---------------------------------------------

    for _ in range(8):

        plt.figure()
        draw_grid()
        print [poly.hatch for poly in polys]

        # shift polygons by one position
        temp_circumcircle = polys[0].circumcircle
        for i in range(len(polys)-1):
            polys[i].circumcircle = polys[i+1].circumcircle

        polys[len(polys)-1].circumcircle = temp_circumcircle

        # temp_hatch = polys[len(polys)-1].hatch
        # for i in range(len(polys)-1)[1:][::-1]:
        #     polys[i].hatch = polys[i-1].hatch
        #     # polys[i].rotate(math.pi/2)
        # polys[0].hatch = temp_hatch

        for i in range(len(polys)):
            # polys[i].circumcircle =temp_polys[i].circumcircle
            # polys[i].hatch = '*' if i%2 == 0 else '\\'
            polys[i].gen_points()
            polys[i].drawPolygon()

        plt.axis('off')
        plt.axis('image')
        plt.savefig('./grid'+str(_)+'.png', dpi=150)

        img = cv2.imread('./grid'+str(_)+'.png', 0)
        img = cropImage(img)
        cv2.imwrite('./grid'+str(_)+'.png', img)

    os.system(
        'montage -mode concatenate -tile 5x1 -border 5 grid.png grid[0-3].png grid_final.png')
    names = ['grid4.png', 'grid5.png', 'grid6.png', 'grid7.png']
    random.shuffle(names)
    os.system('montage -mode concatenate -tile 4x1 -border 5 ' +
              ' '.join(names)+' grid_options.png')

    # LOGIC2 ends
    ##################################################################################


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
