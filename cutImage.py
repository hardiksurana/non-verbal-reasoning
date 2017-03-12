from Polygons.Polygons import Polygon,plt
from Polygons.utils import cropImage,splitQuad

import random
import cv2

for l in range(10):
        #Cleans canvas starts a new figure 
        plt.figure()
    
        # Make a random polygon (the outer most Polygon) 
        A = Polygon( )
        A.makeRandom()
        A.drawPolygon()

        # This stores the polgons that make up an image.
        # We should store this and use it to create a distractor image
        seqs_of_polygons = [A]

        # make 5 Polygon inside it
        for j in range(5):
            # any number of sides 
            B = Polygon(no_of_sides=int(random.random() * 10)+3)
            # same center and radius
            B.clone_circumcircle(A)
            # Center remains same as A but the radius can be anything less than A's raduis
            B.circumcircle.radius = random.random() * B.circumcircle.radius
            # make the sides 
            B.makeShape()
            # draw the polygon on the canvas
            B.drawPolygon()
            seqs_of_polygons.append(B)
                
        plt.axis('equal')
        # No axis to be drawn
        plt.axis('off')
        # FIX : Save the image in high quality 
        plt.savefig('./plot/plot'+str(l)+'.png')

# Crop those images 
for l in range(10):
    # read image as black and white
    img = cv2.imread('./plot/plot'+str(l)+'.png',0)
    img = cropImage(img)
    # save the cropped image
    cv2.imwrite('./plot/plot'+str(l)+'.png', img)

for l in range(10):
    # read image as black and white
    img = cv2.imread('./plot/plot'+str(l)+'.png',0)

    # Get the any of the quadrant
    # quad,rest_img = splitQuad(img, int(random.random() * 3))
    quad,rest_img = splitQuad(img, 0)
    cv2.imwrite('./plot/quads/plotQuad'+str(l)+'.png',quad)
    cv2.imwrite('./plot/quads/plotRest'+str(l)+'.png',rest_img)
    
        








