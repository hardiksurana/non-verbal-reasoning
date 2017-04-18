from Polygons.Polygons import Polygon,plt,rndangle
import random, os, time, cv2
from Polygons.utils import cropImage,splitQuad

def getrndbool():
    return random.choice([True, False])




# rules = []
# params = []
# funcs = [ "swap_polygons", "rotate", "flip"]


# rule_set_1 = ["flip","rotate"]
# rule_set_2 = ["gen_inside", "add_vertex","rotate"]


# plt.figure()
# Polygons = []
# polys=[]


#######################################################################
'''
A combination of pattern and number of sides repeating 
'''
# odd side have one hatch, even have one hatch. series 
# We don't want XX to be less than 3 
XX = int(random.random()*5)+3

allhatches = Polygon.getHatches()
random.shuffle(allhatches)

SIDE_REPEAT_FREQ = random.choice(range(2,4))
HATCH_REPEAT_FREQ = random.choice(range(2,4))
TOTAL_FIG = 2 * max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ)

# Pick any N indexs
rndindex = int(random.random() * (len(allhatches)-HATCH_REPEAT_FREQ) )
two_hatches = allhatches[ rndindex : rndindex+HATCH_REPEAT_FREQ]

# +4 FOR GENERATING DISTRACTORS
for i in range(TOTAL_FIG+6):
    plt.figure()
    A = Polygon(no_of_sides= 3+(XX+i)%SIDE_REPEAT_FREQ, isRegular=False, hatch= two_hatches[(XX+i)%HATCH_REPEAT_FREQ])
    A.makeRandomCircumcircle()
    # polys.append(A)
    A.drawPolygon()
    plt.axis('off') 
    plt.axis('image')
    if i< TOTAL_FIG:
        plt.savefig('./plot/series/'+str(i)+'.png')
        img = cv2.imread('./plot/series/'+str(i)+'.png',0)
        img = cropImage(img)
        # save the cropped image
        cv2.imwrite('./plot/series/'+str(i)+'.png', img)
        os.system(' convert '+'./plot/series/'+str(i)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/series/'+str(i)+'.png')
    else:
        plt.savefig('./plot/series/dist'+str(i-TOTAL_FIG)+'.png')
        img = cv2.imread('./plot/series/dist'+str(i-TOTAL_FIG)+'.png',0)
        img = cropImage(img)
        # save the cropped image
        cv2.imwrite('./plot/series/dist'+str(i-TOTAL_FIG)+'.png', img)
        os.system(' convert '+'./plot/series/dist'+str(i-TOTAL_FIG)+'.png'+'  -bordercolor Black -border 4x4 '+'./plot/series/dist'+str(i-TOTAL_FIG)+'.png')

ID = str(time.time())
print('montage -mode concatenate -tile '+str(TOTAL_FIG)+'x1 ./plot/series/[0-'+str(TOTAL_FIG-1)+'].png ./plot/series/'+ID+'.png')
os.system('montage -mode concatenate -tile '+str(TOTAL_FIG)+'x1 ./plot/series/[0-'+str(TOTAL_FIG-1)+'].png ./plot/series/'+ID+'.png')
# print('montage -mode concatenate -tile 4x1 ./plot/series/['+str(TOTAL_FIG-1)+'-'+str(TOTAL_FIG+2)+'].png ./plot/series/'+ID+'dist.png')
a = map(str,range(max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ)))
random.shuffle(a)
print(a, ','.join(a))

filename = ''
for i in a:
    filename+= ' ./plot/series/dist'+i+'.png'



os.system('montage -mode concatenate -tile '+str(max(SIDE_REPEAT_FREQ, HATCH_REPEAT_FREQ))+'x1 '+filename+' ./plot/series/'+ID+'dist.png')


#############################################################################




# plt.figure()
# for i in range(len(polys)):
#     if i%2 != 0:
#         polys[i].gen_inside(polys[i-1])
#         polys[i].drawPolygon()
#         plt.axis('off') 
#         plt.axis('image')
#         plt.savefig('./series'+str(i)+'.png')
#         plt.figure()
#     else:
#         polys[i].drawPolygon()
#         plt.axis('off') 
#         plt.axis('image')
#         plt.savefig('./series'+str(i)+'.png')

# rules = ['gen_inside','gen_outside','flip']
# for l in range(3):
#     rulen_index = int(random.random()) * len(rules)
#     plt.figure()
#     counter = 0
#     for i in range(len(polys)-1):
#         fig = plt.figure()
#         # rules[]

#         polys[i+1].gen_inside(polys[i])
#         for j in range(2):
#             polys[i+j].drawPolygon()
#         plt.axis('off') 
#         plt.axis('image')
#         plt.savefig('./plot/series/series_'+str(l)+'_'+str(counter)+'.png')
#         plt.close(fig)
#         counter += 1


