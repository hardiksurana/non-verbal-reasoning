from Polygons.Polygons import Polygon,plt,rndangle
from Polygons.utils import cropImage,splitQuad
import math
import random
import cv2

transformations = ['delete_vertex','add_vertex','flip','']
seq = ['add']*3
print('seq',seq)



# a list of polygons and what func_names to be applied and with what params
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
            poly[i].swap_polygons(otherpoly=params[i]['otherpoly'])


for l in range(3):
        #Cleans canvas starts a new figure 
        plt.figure()
    
        # Make a random polygon (the outer most Polygon) 
        A = Polygon( )
        A.makeRandomCircumcircle()
        # A.drawPolygon()

        # This stores the polgons that make up an image.
        # We should store this and use it to create a distractor image
        seqs_of_polygons = []

        # make 5 Polygon inside it
        for j in range(3):
            # any number of sides 
            B = Polygon(no_of_sides=int(random.random() * 3)+3)
            # same center and radius
            B.clone_circumcircle(A)
            # Center remains same as A but the radius can be anything less than A's raduis
            B.circumcircle.radius = 0.5 * A.circumcircle.radius
            # make the sides 
            B.makeShape()
            # draw the polygon on the canvas
            B.drawPolygon()
            seqs_of_polygons.append(B)
            A.circumcircle.radius = B.circumcircle.radius
                
        plt.axis('image')
        plt.axis('off')
        # No axis to be drawn
        # FIX : Save the image in high quality 
        plt.savefig('./plot/trans/plot'+str(l)+'.png')
        img = cv2.imread('./plot/trans/plot'+str(l)+'.png',0)
        img = cropImage(img)    
        cv2.imwrite('./plot/trans/plot'+str(l)+'.png',img)
        

        plt.figure()    
        for i in range(len(seqs_of_polygons)):
            if i == 0:
                seqs_of_polygons[i].flip()
            elif i == 1:
                seqs_of_polygons[i].rotate(math.pi * 0.5)
            elif i == 2:
                seqs_of_polygons[i].flip('hori')
            elif i == 3:
                seqs_of_polygons[i].rotate(math.pi * 0.75)
            seqs_of_polygons[i].drawPolygon()

        plt.axis('image')
        plt.axis('off')
        plt.savefig('./plot/trans/plotTransform'+str(l)+'.png')   

for l in range(3):

    # read image as black and white
    img = cv2.imread('./plot/trans/plotTransform'+str(l)+'.png',0)
    img = cropImage(img)    
    cv2.imwrite('./plot/trans/plotTransform'+str(l)+'.png',img)





