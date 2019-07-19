from src.Polygons.Polygons import Polygon,plt,rndangle
from src.Polygons.utils import cropImage,splitQuad
import random, os, time, cv2

# def getrndbool():
#     return random.choice([True, False])




# rules = []
# params = []
# funcs = [ "swap_polygons", "rotate", "flip"]


# rule_set_1 = ["flip","rotate"]
# rule_set_2 = ["gen_inside", "add_vertex","rotate"]


# plt.figure()
# Polygons = []
# polys=[]


# # #######################################################################
# '''
# A combination of pattern and number of sides repeating 
# '''

# # odd side have one hatch, even have one hatch. series 
# # We don't want XX to be less than 3 
# XX = int(random.random()*5)+3

# allhatches = Polygon.getHatches()
# random.shuffle(allhatches)

# SIDE_REPEAT_FREQ = random.choice(range(2,4))
# HATCH_REPEAT_FREQ = random.choice(range(2,4))
# TOTAL_FIG = 2 * max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ)

# # Pick any N indexs
# rndindex = int(random.random() * (len(allhatches)-HATCH_REPEAT_FREQ) )
# two_hatches = allhatches[ rndindex : rndindex+HATCH_REPEAT_FREQ]

# # +4 FOR GENERATING DISTRACTORS
# for i in range(TOTAL_FIG+6):
#     plt.figure()
#     A = Polygon(no_of_sides= 3+(XX+i)%SIDE_REPEAT_FREQ, isRegular=False, hatch= two_hatches[(XX+i)%HATCH_REPEAT_FREQ])
#     A.makeRandomCircumcircle()
#     # polys.append(A)
#     A.drawPolygon()
#     plt.axis('off') 
#     plt.axis('image')
#     if i< TOTAL_FIG:
#         plt.savefig('./plot/series/'+str(i)+'.png')
#         img = cv2.imread('./plot/series/'+str(i)+'.png',0)
#         img = cropImage(img)
#         # save the cropped image
#         cv2.imwrite('./plot/series/'+str(i)+'.png', img)
#         os.system(' convert '+'./plot/series/'+str(i)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/series/'+str(i)+'.png')
#     else:
#         plt.savefig('./plot/series/dist'+str(i-TOTAL_FIG)+'.png')
#         img = cv2.imread('./plot/series/dist'+str(i-TOTAL_FIG)+'.png',0)
#         img = cropImage(img)
#         # save the cropped image
#         cv2.imwrite('./plot/series/dist'+str(i-TOTAL_FIG)+'.png', img)
#         os.system(' convert '+'./plot/series/dist'+str(i-TOTAL_FIG)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/series/dist'+str(i-TOTAL_FIG)+'.png')

# ID = str(time.time())
# print('montage -mode concatenate -tile '+str(TOTAL_FIG)+'x1 ./plot/series/[0-'+str(TOTAL_FIG-1)+'].png ./plot/series/'+ID+'.png')
# os.system('montage -mode concatenate -tile '+str(TOTAL_FIG)+'x1 ./plot/series/[0-'+str(TOTAL_FIG-1)+'].png ./plot/series/'+ID+'.png')
# # print('montage -mode concatenate -tile 4x1 ./plot/series/['+str(TOTAL_FIG-1)+'-'+str(TOTAL_FIG+2)+'].png ./plot/series/'+ID+'dist.png')
# a = map(str,range(max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ)))
# random.shuffle(a)
# print(a, ','.join(a))

# filename = ''
# for i in a:
#     filename+= ' ./plot/series/dist'+i+'.png'



# os.system('montage -mode concatenate -tile '+str(max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ))+'x1 '+filename+' ./plot/series/'+ID+'dist.png')


# #############################################################################


"""
polys = []

TOTAL_FIG = 6

for i in range(TOTAL_FIG):
    plt.figure()
    A = Polygon(no_of_sides= 3+int(random.random()*10), isRegular=True, hatch=None)
    A.makeRandomCircumcircle()
    polys.append(A)
    A.drawPolygon()
    # plt.axis('off') 
    # plt.axis('image')

plt.figure()
for i in range(len(polys)):
    if i%2 != 0:
        polys[i].gen_inside(polys[i-1])
        polys[i-1].hatch = None
        polys[i].hatch = 'random'
        polys[i].drawPolygon()
        plt.axis('off') 
        plt.axis('image')
        plt.savefig('./series'+str(i)+'.png')
        plt.figure()
    else:
        polys[i].drawPolygon()
        plt.axis('off') 
        plt.axis('image')
        plt.savefig('./series'+str(i)+'.png')

rules = ['gen_inside','gen_outside','flip']
for l in range(3):
    rulen_index = int(random.random()) * len(rules)
    plt.figure()
    counter = 0
    for i in range(len(polys)-1):
        fig = plt.figure()
        # rules[]

        polys[i+1].gen_inside(polys[i])
        polys[i+1].hatch = None
        polys[i].hatch = 'random'
        for j in range(2):
            polys[i+j].drawPolygon()
        plt.axis('off') 
        plt.axis('image')
        plt.savefig('./plot/series/series_'+str(l)+'_'+str(counter)+'.png')
        plt.close(fig)
        counter += 1
"""

# #############################################################################

class Series:
    '''
    A combination of pattern and number of sides repeating 
    '''
    def __init__(self, user_id, session_id, questionCount):
        self.user_id = str(user_id)
        self.session_id = str(session_id)
        self.questionCount = questionCount
        self.question_path = ''
        self.answer_path = ''
        self.distractors_path = []
        self.STATIC_ROOT = os.path.join(os.getcwd(), "src/webapp/static/")

        # odd side have one hatch, even have one hatch. series 
        self.XX = int(random.random()*5)+3
        self.allhatches = Polygon.getHatches()
        random.shuffle(self.allhatches)
        self.SIDE_REPEAT_FREQ = random.choice(range(2,4))
        self.HATCH_REPEAT_FREQ = random.choice(range(2,4))
        # self.TOTAL_FIG = 2 * max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ)
        self.TOTAL_FIG = 6

        # Pick any N indexs
        self.rndindex = int(random.random() * (len(self.allhatches)-self.HATCH_REPEAT_FREQ) )
        self.two_hatches = self.allhatches[ self.rndindex : self.rndindex+self.HATCH_REPEAT_FREQ]
    
    def generate_all_images(self):
        for i in range(1, self.TOTAL_FIG+4):
            plt.figure()
            A = Polygon(no_of_sides= 3+(self.XX+i)%self.SIDE_REPEAT_FREQ, isRegular=False, hatch= self.two_hatches[(self.XX+i)%self.HATCH_REPEAT_FREQ])
            A.makeRandomCircumcircle()
            A.drawPolygon()
            plt.axis('image')
            plt.axis('off') 

            # part of the question
            if i < self.TOTAL_FIG:
                question_tmpPath = self.STATIC_ROOT + 'tmp/' + self.user_id + "_" + self.session_id + '_series_question_'+str(self.questionCount)+'_part_' + str(i) + '.png'
                plt.savefig(question_tmpPath)
                plt.close()
                img = cv2.imread(question_tmpPath,0)
                img = cropImage(img)
                cv2.imwrite(question_tmpPath, img)
                os.system(' convert '+question_tmpPath+'  -bordercolor Black -border 4x4 '+question_tmpPath)
            
            # answer
            elif i == self.TOTAL_FIG:
                self.answer_path = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_series_answer_'+str(self.questionCount)+'.png'
                plt.savefig(self.answer_path)
                plt.close()
                img = cv2.imread(self.answer_path,0)
                img = cropImage(img)
                cv2.imwrite(self.answer_path, img)
                os.system(' convert '+self.answer_path+'  -bordercolor Black -border 4x4 '+self.answer_path)
            
            # distractors
            else:
                distractor_path = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_series_question_'+str(self.questionCount)+'_dist_'+str(i-self.TOTAL_FIG-1)+'.png'
                plt.savefig(distractor_path)
                plt.close()
                img = cv2.imread(distractor_path,0)
                img = cropImage(img)
                cv2.imwrite(distractor_path, img)
                os.system(' convert '+distractor_path+'  -bordercolor Black -border 4x4 '+distractor_path)
                self.distractors_path.append(distractor_path)
        
        # build question montage
        question_path = self.STATIC_ROOT + 'tmp/' + self.user_id + "_" + self.session_id + '_series_question_'+str(self.questionCount)+'_part_'
        self.question_path = self.STATIC_ROOT + 'result/' + self.user_id + "_" + self.session_id + '_series_question_'+str(self.questionCount)+'.png'

        os.system('montage -mode concatenate -tile '+str(self.TOTAL_FIG-1)+'x1 ' + question_path + '[1-'+str(self.TOTAL_FIG-1)+'].png ' + self.question_path)

    def get_question(self):
        return self.question_path
    
    def get_answer(self):
        return self.answer_path
    
    def get_distractors(self):
        return self.distractors_path

if __name__ == "__main__":
    s = Series(1, 'abc', 1)
    s.generate_all_images()
