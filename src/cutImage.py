from Polygons.Polygons import Polygon,plt
from Polygons.utils import cropImage,splitQuad

import random, cv2, math, os

NO_OF_FIGURES_IN_ONE = 3
NO_OF_EXAMPLES = 10


def draw_boundary(quad_number,filename):
    img = cv2.imread(filename,0)
    print img.shape
    print filename
    height, width = img.shape
    if quad_number == 0:
        os.system('convert '+filename+' -stroke black -fill white -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+',0 '+str(width/2)+','+str(height/2)+'\" ' + filename )
        # print('convert '+filename+' -fill white -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+',0 '+str(width/2)+','+str(height/2)+'\" ' + filename )
    elif quad_number == 1:
        os.system('convert '+filename+' -stroke black -fill white -draw \"stroke-dasharray 5 3 rectangle 0,0 '+str(width/2)+','+str(height/2)+'\" ' + filename)
        # print('convert '+filename+' -fill white -draw \"stroke-dasharray 5 3 rectangle 0,0 '+str(width/2)+','+str(height)+'\" ' + filename)
    elif quad_number == 2:
        os.system('convert '+filename+' -stroke black -fill white -draw \"stroke-dasharray 10 4 rectangle 0,'+str(height/2)+' '+str(width/2)+','+str(height)+'\" ' + filename)
        # print('convert '+filename+' -fill white -draw \"stroke-dasharray 5 3 rectangle 0,'+str(height/2)+' '+str(width/2)+','+str(height/2)+'\" ' + filename)
    elif quad_number == 3:
        os.system('convert '+filename+' -stroke black -fill white -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+','+str(height/2)+' '+str(width)+','+str(height)+'\" ' + filename)
        # print('convert '+filename+' -fill black -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+','+str(height/2)+' '+str(width/2)+','+str(height/2)+'\" ' + filename )


def apply(polys,func_names,params):
    assert len(polys) == len(func_names) and len(func_names) == len(params)
    for i in range(len(polys)):
        
        if func_names[i] == 'flip':
            # apply something on the object
            polys[i].flip(how=params[i]['how'])
        elif func_names[i] == 'rotate':
            polys[i].rotate(theta=params[i]['theta'])
        elif func_names[i] == 'add_vertex':
            polys[i].add_vertex()
        elif func_names[i] == 'delete_vertex':
            polys[i].delete_vertex()
        elif func_names[i] == 'clone_circumcircle':
            polys[i].clone_circumcircle(otherpoly=params[i]['otherpoly'])
        elif func_names[i] == 'setHatch':
            polys[i].setHatch(hatch=params[i]['hatch'])
        elif func_names[i] == 'swap_polygons':
            polys[i].swap_polygons(otherpoly=params[i]['otherpoly'])

'''
for l in range(NO_OF_EXAMPLES):
    
    #Cleans canvas starts a new figure 
    plt.figure()

    # Make a random polygon (the outer most Polygon) 
    A = Polygon( )
    A.makeRandomCircumcircle()
    A.drawPolygon()

    # This stores the polgons that make up an image.
    # We should store this and use it to create a distractor image
    seqs_of_polygons = [A]


    polys = []
    # make 5 Polygon inside it
    for j in range(NO_OF_FIGURES_IN_ONE):
        # any number of sides 
        B = Polygon(no_of_sides=random.choice([0,int(random.random()*7)+3]),isRegular='any',hatch=None)
        # same center and radius
        B.clone_circumcircle(A)

        # since cutImage questions they should be symmetric 

        B.circumcircle.x = B.circumcircle.x #+ random.choice([1,-1]) * random.choice(range(1,5))
        B.circumcircle.y = B.circumcircle.y #+ random.choice([1,-1]) * random.choice(range(1,5))
        # Center remains same as A but the radius can be anything less than A's raduis
        # B.circumcircle.radius = random.choice([0.2,0.4,0.8]) * B.circumcircle.radius
        B.circumcircle.radius = random.choice([10,20,40,50]) + B.circumcircle.radius
        # make the sides 
        B.makeShape()
        # draw the polygon on the canvas
        B.drawPolygon()
        seqs_of_polygons.append(B)
            
    plt.axis('image')
    plt.axis('off')

    # No axis to be drawn
        # FIX : Save the image in high quality 
    plt.savefig('./plot/plot'+str(l)+'.png')



    # Distractor images
    for j in range(3):
        # how many distractor images 
        plt.figure()
        for i  in seqs_of_polygons:
            # do something and then draw the distractors.
            choice = random.choice(['flip','rotate','swap'])
            if choice == 'flip':
                i.flip(how=random.choice(['vert','hori']))
            elif choice == 'rotate':
                i.rotate(theta=random.choice([math.pi/2, math.pi/4, math.pi]))
            elif choice=='swap':
                i.swap_polygons(random.choice(seqs_of_polygons))

            i.drawPolygon()

        plt.axis('image')
        plt.axis('off')

        # No axis to be drawn
            # FIX : Save the image in high quality 
        plt.savefig('./plot/plot'+str(l)+'Dist'+str(j)+'.png')

print "DRAW DONE."
# raw_input()

# Crop those images 
for l in range(NO_OF_EXAMPLES):
    # read image as black and white
    img = cv2.imread('./plot/plot'+str(l)+'.png',0)
    img = cropImage(img)
    # save the cropped image
    cv2.imwrite('./plot/plot'+str(l)+'.png', img)


    for j in range(3):
            # how many distractor images    
        img = cv2.imread('./plot/plot'+str(l)+'Dist'+str(j)+'.png',0)
        img = cropImage(img)
        # save the cropped image
        cv2.imwrite('./plot/plot'+str(l)+'Dist'+str(j)+'.png', img)

print "CROP DONE."
# raw_input()

for l in range(NO_OF_EXAMPLES):
    # read image as black and white
    
    img = cv2.imread('./plot/plot'+str(l)+'.png',0)

    # Get the any of the quadrant
    # quad,rest_img = splitQuad(img, int(random.random() * 3))
    quad_number = random.choice([0,1,2,3])
    quad,rest_img = splitQuad(img, quad_number)
    cv2.imwrite('./plot/quads/plotQuad'+str(l)+'.png',quad)
    cv2.imwrite('./plot/quads/plotRest'+str(l)+'.png',rest_img)

    # draw dotted line for rest_img
    draw_boundary(quad_number,'./plot/quads/plotRest'+str(l)+'.png')

    os.system(' convert '+'./plot/quads/plotRest'+str(l)+'.png'+'  -bordercolor Black -border 8x8 '+'./plot/quads/plotRest'+str(l)+'.png')
    os.system(' convert '+'./plot/quads/plotQuad'+str(l)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/quads/plotQuad'+str(l)+'.png')
    

    for j in range(3):
        # how many distractor images
        
        img = cv2.imread('./plot/plot'+str(l)+'Dist'+str(j)+'.png',0)

        # Get the any of the quadrant
        # quad,rest_img = splitQuad(img, int(random.random() * 3))
        # get the same as above had been done 
        quad,rest_img = splitQuad(img, quad_number)
        cv2.imwrite('./plot/quads/plotQuad'+str(l)+'Dist'+str(j)+'.png',quad)
        cv2.imwrite('./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png',rest_img)

        # Add border
        os.system(' convert '+'./plot/quads/plotQuad'+str(l)+'Dist'+str(j)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/quads/plotQuad'+str(l)+'Dist'+str(j)+'.png')
        os.system(' convert '+'./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png'+'  -bordercolor Black -border 8x8 '+'./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png')
        
    names = ['./plot/quads/plotQuad'+str(l)+'.png', './plot/quads/plotQuad'+str(l)+'Dist0.png', './plot/quads/plotQuad'+str(l)+'Dist1.png', './plot/quads/plotQuad'+str(l)+'Dist2.png', ] 
    random.shuffle(names)
    os.system('montage -tile 4x1 '+' '.join(names)+' ./plot/quads/output'+str(l)+'.png')
        # img = cv2.imread('./plot/plot'+str(l)+'Dist'+str(j)+'.png',0)
        # img = cropImage(img)
        # # save the cropped image
        # cv2.imwrite('./plot/plot'+str(l)+'Dist'+str(j)+'.png', img)

'''

class Cut:
    def __init__(self, polyNum, questionCount, setCount, optionNum):
        self.polyNum = polyNum
        self.questionCount = questionCount
        self.setCount = setCount
        self.optionNum = optionNum
        # self.sidesNum = sidesNum
        self.question_path = ''
        self.answer_path = ''
        self.distractors = []
        self.distractors_path = []
        self.quadrantNum = random.choice([0,1,2,3])
        self.STATIC_ROOT = '/Users/hardik/Desktop/projects/turtle/src/webapp/static/'
    
    def genQuestionAnswerPair(self):
        # generate question image 
        plt.figure()

        # Make a random polygon (the outer most Polygon) 
        A = Polygon()
        A.makeRandomCircumcircle()
        A.drawPolygon()

        # This stores the polygons that make up an image.
        # We should store this and use it to create a distractor image
        seqs_of_polygons = [A]
        polys = []

        # make 5 Polygons inside it
        for j in range(self.polyNum):
            # any number of sides 
            B = Polygon(no_of_sides=random.choice([0,int(random.random()*7)+3]),isRegular='any',hatch=None)
            # same center and radius
            B.clone_circumcircle(A)

            # since cutImage questions they should be symmetric 
            B.circumcircle.x = B.circumcircle.x
            B.circumcircle.y = B.circumcircle.y
            B.circumcircle.radius = random.choice([10,20,40,50]) + B.circumcircle.radius
            # make the sides 
            B.makeShape()
            # draw the polygon on the canvas
            B.drawPolygon()
            seqs_of_polygons.append(B)
                
        self.distractors = seqs_of_polygons

        plt.axis('image')
        plt.axis('off')
        question_tmpPath = self.STATIC_ROOT + 'tmp/set_' + str(self.setCount) + '_question_'+str(self.questionCount)+'.png'
        plt.savefig(question_tmpPath)

        # crop the question image
        img = cv2.imread(question_tmpPath, 0)
        img = cropImage(img)
        cv2.imwrite(question_tmpPath, img)

        # remove one quadrant from question and generate answer
        self.question_path = self.STATIC_ROOT + 'result/set_' + str(self.setCount) + '_question_'+str(self.questionCount)+'.png'
        self.answer_path = self.STATIC_ROOT + 'result/set_' + str(self.setCount) + '_answer_'+str(self.questionCount)+'.png'

        img = cv2.imread(question_tmpPath, 0)
        quad, rest_img = splitQuad(img, self.quadrantNum)
        cv2.imwrite(self.answer_path, quad)
        cv2.imwrite(self.question_path, rest_img)
        draw_boundary(self.quadrantNum, self.question_path)
        os.system(' convert '+ self.question_path +'  -bordercolor Black -border 8x8 '+ self.question_path)
        os.system(' convert '+ self.answer_path +'  -bordercolor Black -border 4x4 '+ self.answer_path)


    def genDistractors(self):
        # generate distractor images
        for j in range(self.optionNum):
            plt.figure()
            for i  in self.distractors:
                # do something and then draw the distractors.
                choice = random.choice(['flip', 'rotate', 'swap'])
                if choice == 'flip':
                    i.flip(how=random.choice(['vert', 'hori']))
                elif choice == 'rotate':
                    i.rotate(theta=random.choice([math.pi/2, math.pi/4, math.pi]))
                elif choice=='swap':
                    i.swap_polygons(random.choice(self.distractors))

                i.drawPolygon()

            plt.axis('image')
            plt.axis('off')

            distractor_tmpPath = self.STATIC_ROOT + 'tmp/set_' + str(self.setCount) + '_question_'+str(self.questionCount)+'_dist_'+str(j)+'.png'
            plt.savefig(distractor_tmpPath)

            # crop the image
            img = cv2.imread(distractor_tmpPath, 0)
            img = cropImage(img)
            cv2.imwrite(distractor_tmpPath, img)

            # remove one quadrant from distractor full image and generate options
            img = cv2.imread(distractor_tmpPath, 0)
            quad, rest_img = splitQuad(img, self.quadrantNum)

            distractor_finalPath = self.STATIC_ROOT + 'result/set_' + str(self.setCount) + '_question_'+str(self.questionCount)+'_dist_'+str(j)+'.png'
            cv2.imwrite(distractor_finalPath, quad)
            # cv2.imwrite('./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png',rest_img)

            self.distractors_path.append(os.path.split(distractor_finalPath)[1])

            # add border
            os.system(' convert ' + distractor_finalPath + '  -bordercolor Black -border 4x4 ' + distractor_finalPath)
            # os.system(' convert '+'./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png'+'  -bordercolor Black -border 8x8 '+'./plot/quads/plotRest'+str(l)+'Dist'+str(j)+'.png')
    
    def getQuestion(self):
        return os.path.split(self.question_path)[1]
    
    def getAnswer(self):
        return os.path.split(self.answer_path)[1]
    
    def getDistractors(self):
        return self.distractors_path
    