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
        os.system('convert '+filename+' -fill none -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+',0 '+str(width/2)+','+str(height)+'\" ' + filename )
    elif quad_number == 1:
        os.system('convert '+filename+' -fill none -draw \"stroke-dasharray 5 3 rectangle 0,0 '+str(width/2)+','+str(height)+'\" ' + filename)
    elif quad_number == 2:
        os.system('convert '+filename+' -fill none -draw \"stroke-dasharray 5 3 rectangle 0,'+str(height/2)+' '+str(width/2)+','+str(height)+'\" ' + filename)
    elif quad_number == 3:
        os.system('convert '+filename+' -fill none -draw \"stroke-dasharray 5 3 rectangle '+str(width/2)+','+str(height/2)+' '+str(width/2)+','+str(height)+'\" ' + filename)


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
            B.circumcircle.radius = random.choice([0.2,0.4,0.8]) * B.circumcircle.radius
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

    os.system('montage -tile 4x1 '+'./plot/quads/plotQuad'+str(l)+'.png ./plot/quads/plotQuad'+str(l)+'Dist[0-2].png ./plot/quads/output'+str(l)+'.png')
        # img = cv2.imread('./plot/plot'+str(l)+'Dist'+str(j)+'.png',0)
        # img = cropImage(img)
        # # save the cropped image
        # cv2.imwrite('./plot/plot'+str(l)+'Dist'+str(j)+'.png', img)





    