from Polygons.Polygons import Polygon,plt,rndangle,Circumcircle
from Polygons.utils import cropImage,splitQuad

import math,copy
import random
import cv2
import string

 


def draw_type(layout_type=1):
    """
    This will draw a type.
    """
    # More randomnes unique
    symbols = ["#","-","*","**","^","?"]
    # symbols = [random.choice(['#','*','1','-','?','2','^']) for i in range(6)]
    # symbols = [1,2,3,4,5,6]

    side = 10
    X_base = 0
    Y_base = 0
    zoom=3

    triplets = [ (2,1,5),(2,1,6),(2,3,5),(2,3,6),
                 (4,1,6),(4,1,5),(4,3,6),(4,3,5)]

    wrong_triplets = [ (2,1,4),(2,5,4),(2,6,4),(2,3,4)] 

    plt.figure()


    # Firs four are always drawn the same way
    for i in range(4):
            # draw 1-4
            polygon = plt.Rectangle((0,-i*side),side,side,fill=False)
            plt.gca().text(side/2, -(i*side-side/2), symbols[i],
                        # rotation value should in degrees
                        # rotation=self.alphabet_rotation * (180/math.pi) ,
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                        # fontproperties=zhfont1
                    )
            plt.gca().add_patch(polygon)


    if layout_type == 1:
        
        #  Type 1
        #   1
        #   |
        # 5-2-6       
        #   |          
        #   3
        #   |
        #   4
        # 
        # 2-1-5 
        # 2-1-6
        # 2-3-5
        # 2-3-6
        # 4-1-6
        # 4-1-5
        # 4-3-6
        # 4-3-5

        # Draw 5
        polygon = plt.Rectangle((-side,-side),side,side,fill=False)
        plt.gca().text(-side/2, -side/2, symbols[4],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

        # # Draw 6
        polygon = plt.Rectangle((side,-side),side,side,fill=False)
        plt.gca().text(side+side/2, -side/2, symbols[5],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)
    elif layout_type == 2:
        #  Type 2
        # 5-1
        #   |
        #   2-6       
        #   |          
        #   3
        #   |
        #   4
        # 
        # 2-1-5 
        # 2-1-6
        # 2-3-5
        # 2-3-6
        # 4-1-6
        # 4-1-5
        # 4-3-6
        # 4-3-5

        # Draw 5
        polygon = plt.Rectangle((-side,0),side,side,fill=False)
        plt.gca().text(-side/2, +side/2, symbols[4],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

        # # Draw 6
        polygon = plt.Rectangle((side,-side),side,side,fill=False)
        plt.gca().text(side+side/2, -side/2, symbols[5],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)
    elif layout_type == 3:
        # pass
        #  Type 2
        #   1
        #   |
        # 5-2       
        #   |          
        #   3-6
        #   |
        #   4
        # 
        # 2-1-5 
        # 2-1-6
        # 2-3-5
        # 2-3-6
        # 4-1-6
        # 4-1-5
        # 4-3-6
        # 4-3-5

        # Draw 5
        polygon = plt.Rectangle((-side,-side),side,side,fill=False)
        plt.gca().text(-side/2, -side/2, symbols[4],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

        # # Draw 6
        polygon = plt.Rectangle((side,-2*side),side,side,fill=False)
        plt.gca().text(side+side/2, -side/2-side, symbols[5],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

    elif layout_type == 4:
        
        #  Type 2
        # 5-1
        #   |
        #   2      
        #   |          
        #   3-6
        #   |
        #   4
        
        # Draw 5
        polygon = plt.Rectangle((-side,0),side,side,fill=False)
        plt.gca().text(-side/2, -side/2+side, symbols[4],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

        # # Draw 6
        polygon = plt.Rectangle((side,-2*side),side,side,fill=False)
        plt.gca().text(side+side/2, -side/2-side, symbols[5],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)
    elif layout_type == 5:
        
        #  Type 2
        #   1
        #   |
        # 5-2      
        #   |          
        #   3
        #   |
        #   4-6
        # 
       
        # Draw 5
        polygon = plt.Rectangle((-side,-side),side,side,fill=False)
        plt.gca().text(-side/2, -side/2, symbols[4],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)

        # # Draw 6
        polygon = plt.Rectangle((side,-3*side),side,side,fill=False)
        plt.gca().text(side+side/2, -side/2-2*side, symbols[5],
                    # rotation value should in degrees
                    # rotation=self.alphabet_rotation * (180/math.pi) ,
                    fontsize=zoom*side,
                    multialignment='center',
                    verticalalignment='center', horizontalalignment='center',
                    # fontproperties=zhfont1
                )
        plt.gca().add_patch(polygon)





        
    plt.axis('image')
    plt.axis('off')
    plt.savefig('./dicelayout.png')  

    for i in range(3):
        temp_triplet = random.choice(triplets)
        draw_three([symbols[j-1] for j in temp_triplet],'dice'+str(i+1))

    for i in range(3):
        temp_triplet = random.choice(wrong_triplets)
        draw_three([symbols[j-1] for j in temp_triplet],'dice_'+str(i+1))
"""
Takes three symbols and generates the adjacent three faces of a dice.
And saves that to a file.
"""
def draw_three(symbols,name):    
    plt.figure()
    side = 10
    zoom = 3
    angle = math.pi/8
    polygon = plt.Polygon([(0,0),(0,-side),(side*math.cos(angle),side*math.sin(angle)-side),(side*math.cos(angle),side*math.sin(angle))],fill=False)
    plt.gca().add_patch(polygon)
    plt.gca().text(side*math.cos(angle)/2, (side*math.sin(angle)- side)/2, symbols[0],
                        # rotation value should in degrees
                        # rotation=self.alphabet_rotation * (180/math.pi) ,
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                        # fontproperties=zhfont1
                    )

    polygon = plt.Polygon([(0,0),(0,-side),(-side*math.cos(angle),side*math.sin(angle)-side),(-side*math.cos(angle),side*math.sin(angle))],fill=False)
    plt.gca().add_patch(polygon)
    plt.gca().text(-side*math.cos(angle)/2, (side*math.sin(angle)- side)/2, symbols[1],
                        # rotation value should in degrees
                        # rotation=self.alphabet_rotation * (180/math.pi) ,
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                        # fontproperties=zhfont1
                    )


    polygon = plt.Polygon([(0,0),(side*math.cos(angle),side*math.sin(angle)),(0,2*side*math.sin(angle)),(-side*math.cos(angle),side*math.sin(angle)) ],fill=False)
    plt.gca().add_patch(polygon)
    plt.gca().text(0, side*math.sin(angle),symbols[2],
                        # rotation value should in degrees
                        # rotation=self.alphabet_rotation * (180/math.pi) ,
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                         # fontproperties=zhfont1
                    )

    plt.axis('image')
    plt.axis('off')
    plt.savefig('./'+name+'.png')   

# draw_three(['3','4','1'],'dice')
draw_type(layout_type=random.choice([1,2,3,4,5]))
# polygon = plt.Polygon([(10,10),(0,10),(),()],fill=False,hatch='/')
# plt.gca().add_patch(polygon)


