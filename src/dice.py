from Polygons.Polygons import Polygon,plt,rndangle,Circumcircle
from Polygons.utils import cropImage,splitQuad

import math,copy, os
import random
import cv2
import string

 

"""
def draw_type(layout_type=1):
    # More randomnes unique
    # symbols = ["#","-","*","**","^","?"]
    # symbols = random.choice(['1','2','3','4','5','6']
    symbols = ['#','*','-','?','^','**',u'\u2605',u'\u2020',u'\u002B']
    random.shuffle(symbols)
    # symbols = [random.choice(['#','*','1','-','?','2','^','**','**\n*']) for i in range(6)]
    # symbols = [1,2,3,4,5,6]

    side = 10
    X_base = 0
    Y_base = 0
    zoom=3

    triplets = [ (2,5,1),(6,2,1),(2,3,5),(2,3,6),
                 (1,4,6),(4,1,5),(4,6,3),(5,3,4)]

    wrong_triplets = [ (2,1,4),(2,4,5),(4,6,2),(2,3,4)] 

    plt.figure()


    # Firs four are always drawn the same way
    for i in range(4):
            # draw 1-4
            polygon = plt.Rectangle((0,-i*side),side,side,fill=False)
            plt.gca().text(side/2, -(i*side-side/2), symbols[i],
                        # rotation value should in degrees
                        # rotation=self.alphabet_rotation * (180/math.pi) ,
                        fontsize= side * zoom ,
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

    random.shuffle(triplets)
    random.shuffle(wrong_triplets)
 
    for i in range(3):
        temp_triplet = triplets[i]
        draw_three([symbols[j-1] for j in temp_triplet],'dice'+str(i+1))

    for i in range(3):
        temp_triplet = wrong_triplets[i]
        draw_three([symbols[j-1] for j in temp_triplet],'dice_'+str(i+1))
"""


"""
Takes three symbols and generates the adjacent three faces of a dice.
And saves that to a file.
"""

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
"""


#############################################################################
"""
# draw_three(['3','4','1'],'dice')
draw_type(layout_type=random.choice([1,2,3,4,5]))

# CROP and BORDER the laout image
img = cv2.imread('dicelayout.png',0)
img = cropImage(img)
# save the cropped image
cv2.imwrite('dicelayout.png', img)
# os.system(' convert dicelayout.png  -bordercolor Black -border 1x1 dicelayout.png')

# Crop and Add border
names = ['dice_1.png','dice_3.png','dice_2.png','dice1.png']
for i in names:
    img = cv2.imread(i,0)
    img = cropImage(img)
    # save the cropped image
    cv2.imwrite(i, img)
    os.system(' convert '+i+'  -bordercolor Black -border 4x4 '+i)


random.shuffle(names)
os.system('montage -mode concatenate -tile 4x1 -border 10 '+' '.join(names)+' dice_final.png' )

# THis will genrate layout
#

# polygon = plt.Polygon([(10,10),(0,10),(),()],fill=False,hatch='/')
# plt.gca().add_patch(polygon)
"""

#############################################################################

class Dice:
    def __init__(self, user_id, session_id, questionCount):
        self.user_id = str(user_id)
        self.session_id = str(session_id)
        self.questionCount = questionCount
        self.question_path = ''
        self.answer_path = ''
        self.distractors_path = []
        self.STATIC_ROOT = '/Users/hardik/Desktop/projects/turtle/src/webapp/static/'

        self.layout_type = random.choice([1, 2, 3, 4, 5])
        self.symbols = ['#','*','-','?','^','**',u'\u2605',u'\u2020',u'\u002B']
        self.triplets = [(2,5,1), (6,2,1), (2,3,5), (2,3,6), (1,4,6), (4,1,5), (4,6,3), (5,3,4)]
        self.wrong_triplets = [(2,1,4), (2,4,5), (4,6,2), (2,3,4)]
        random.shuffle(self.symbols)
        random.shuffle(self.triplets)
        random.shuffle(self.wrong_triplets)
    
    def generate_question(self):
        side = 10
        X_base = 0
        Y_base = 0
        zoom = 3
        plt.figure()

        # First four are always drawn the same way
        for i in range(4):
                # draw 1-4
                polygon = plt.Rectangle((0,-i*side),side,side,fill=False)
                plt.gca().text(side/2, -(i*side-side/2), self.symbols[i],
                            fontsize= side * zoom ,
                            multialignment='center',
                            verticalalignment='center', horizontalalignment='center',
                        )
                plt.gca().add_patch(polygon)

        if self.layout_type == 1:
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
            plt.gca().text(-side/2, -side/2, self.symbols[4],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

            # Draw 6
            polygon = plt.Rectangle((side,-side),side,side,fill=False)
            plt.gca().text(side+side/2, -side/2, self.symbols[5],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

        elif self.layout_type == 2:
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
            plt.gca().text(-side/2, +side/2, self.symbols[4],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

            # Draw 6
            polygon = plt.Rectangle((side,-side),side,side,fill=False)
            plt.gca().text(side+side/2, -side/2, self.symbols[5],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)
        
        elif self.layout_type == 3:
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
            plt.gca().text(-side/2, -side/2, self.symbols[4],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

            # Draw 6
            polygon = plt.Rectangle((side,-2*side),side,side,fill=False)
            plt.gca().text(side+side/2, -side/2-side, self.symbols[5],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

        elif self.layout_type == 4:
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
            plt.gca().text(-side/2, -side/2+side, self.symbols[4],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

            # Draw 6
            polygon = plt.Rectangle((side,-2*side),side,side,fill=False)
            plt.gca().text(side+side/2, -side/2-side, self.symbols[5],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)
        
        elif self.layout_type == 5:  
            #  Type 2
            #   1
            #   |
            # 5-2      
            #   |          
            #   3
            #   |
            #   4-6

            # Draw 5
            polygon = plt.Rectangle((-side,-side),side,side,fill=False)
            plt.gca().text(-side/2, -side/2, self.symbols[4],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)

            # Draw 6
            polygon = plt.Rectangle((side,-3*side),side,side,fill=False)
            plt.gca().text(side+side/2, -side/2-2*side, self.symbols[5],
                        fontsize=zoom*side,
                        multialignment='center',
                        verticalalignment='center', horizontalalignment='center',
                    )
            plt.gca().add_patch(polygon)
            
        plt.axis('image')
        plt.axis('off')
        question_tmpPath = self.STATIC_ROOT + 'tmp/' + self.user_id + "_" + self.session_id + '_dice_question_'+str(self.questionCount)+'.png'
        plt.savefig(question_tmpPath) 

        # crop the question image
        self.question_path = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_dice_question_'+str(self.questionCount)+'.png'
        img = cv2.imread(question_tmpPath, 0)
        img = cropImage(img)
        cv2.imwrite(self.question_path, img) 

    def draw_three_sides(self, symbols, name):    
        plt.figure()
        side = 10
        zoom = 3
        angle = math.pi/8
        polygon = plt.Polygon([(0,0),(0,-side),(side*math.cos(angle),side*math.sin(angle)-side),(side*math.cos(angle),side*math.sin(angle))],fill=False)
        plt.gca().add_patch(polygon)
        plt.gca().text(side*math.cos(angle)/2, (side*math.sin(angle)- side)/2, symbols[0],
                            fontsize=zoom*side,
                            multialignment='center',
                            verticalalignment='center', horizontalalignment='center',
                        )

        polygon = plt.Polygon([(0,0),(0,-side),(-side*math.cos(angle),side*math.sin(angle)-side),(-side*math.cos(angle),side*math.sin(angle))],fill=False)
        plt.gca().add_patch(polygon)
        plt.gca().text(-side*math.cos(angle)/2, (side*math.sin(angle)- side)/2, symbols[1],
                            fontsize=zoom*side,
                            multialignment='center',
                            verticalalignment='center', horizontalalignment='center',
                        )


        polygon = plt.Polygon([(0,0),(side*math.cos(angle),side*math.sin(angle)),(0,2*side*math.sin(angle)),(-side*math.cos(angle),side*math.sin(angle)) ],fill=False)
        plt.gca().add_patch(polygon)
        plt.gca().text(0, side*math.sin(angle),symbols[2],
                            fontsize=zoom*side,
                            multialignment='center',
                            verticalalignment='center', horizontalalignment='center',
                        )

        plt.axis('image')
        plt.axis('off')
        plt.savefig(name)
    
    def generate_answer(self):
        correct_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        temp_triplet = self.triplets[correct_choice]
        answer_tmpPath = self.STATIC_ROOT + 'tmp/' + self.user_id + "_" + self.session_id + '_dice_answer_'+str(self.questionCount)+'.png'
        self.draw_three_sides([self.symbols[j-1] for j in temp_triplet], answer_tmpPath)
        
        # crop the answer image
        img = cv2.imread(answer_tmpPath, 0)
        img = cropImage(img)
        self.answer_path = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_dice_answer_'+str(self.questionCount)+'.png'
        cv2.imwrite(self.answer_path, img)

    def generate_distractors(self):
        for i in range(3):
            temp_triplet = self.wrong_triplets[i]
            distractor_tmpPath = self.STATIC_ROOT + 'tmp/' + self.user_id + "_" + self.session_id + '_dice_question_'+str(self.questionCount)+'_dist_'+str(i)+'.png'
            self.draw_three_sides([self.symbols[j-1] for j in temp_triplet], distractor_tmpPath)

            # crop the answer image
            img = cv2.imread(distractor_tmpPath, 0)
            img = cropImage(img)
            distractor_finalPath = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_dice_question_'+str(self.questionCount)+'_dist_'+str(i)+'.png'
            cv2.imwrite(distractor_finalPath, img)
            self.distractors_path.append(distractor_finalPath)
    
    def getQuestion(self):
        return self.question_path
    
    def getAnswer(self):
        return self.answer_path
    
    def getDistractors(self):
        return self.distractors_path

if __name__ == "__main__":
    d = Dice(1, 'abc', 1)
    d.generate_question()
    d.generate_answer()
    d.generate_distractors()
