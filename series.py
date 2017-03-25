from Polygons.Polygons import Polygon,plt,rndangle
import random

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

SIDE_REPEAT_FREQ = 3
HATCH_REPEAT_FREQ = 3
TOTAL_FIG = 10

# Pick any N indexs
rndindex = int(random.random() * (len(allhatches)-HATCH_REPEAT_FREQ) )
two_hatches = allhatches[ rndindex : rndindex+HATCH_REPEAT_FREQ]

for i in range(TOTAL_FIG):
    plt.figure()
    A = Polygon(no_of_sides= 3+(XX+i)%SIDE_REPEAT_FREQ, isRegular=False, hatch= two_hatches[(XX+i)%HATCH_REPEAT_FREQ])
    A.makeRandomCircumcircle()
    # polys.append(A)
    A.drawPolygon()
    plt.axis('off') 
    plt.axis('image')
    plt.savefig('./plot/series'+str(i)+'.png')

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


