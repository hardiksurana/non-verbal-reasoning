from Polygons.Polygons import Polygon,plt,rndangle
import random



rules = []
params = []
funcs = [ "swap_polygons", "rotate", "flip"]


rule_set_1 = ["flip","rotate"]
rule_set_2 = ["gen_inside", "add_vertex","rotate"]


plt.figure()
Polygons = []
polys=[]
for i in range(10):
    boolean = (round(random.random()) == 0)
    A = Polygon( no_of_sides= int(random.random()*10) +3, size=random.random()*10, isRegular=boolean)
    A.makeRandomCircumcircle()
    polys.append(A)
    A.drawPolygon()

plt.axis('off') 
plt.axis('image')
plt.savefig('./series.png')


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

rules = ['gen_inside','gen_outside','flip']




for l in range(3):
    rulen_index = int(random.random()) * len(rules)
    plt.figure()
    counter = 0
    for i in range(len(polys)-1):
        fig = plt.figure()
        # rules[]

        polys[i+1].gen_inside(polys[i])

        for j in range(2):
            polys[i+j].drawPolygon()
        plt.axis('off') 
        plt.axis('image')
        plt.savefig('./plot/series/series_'+str(l)+'_'+str(counter)+'.png')
        plt.close(fig)
        counter += 1


