from Polygons.Polygons import Polygon,plt,rndangle
from Polygons.utils import cropImage,splitQuad

import random
import cv2

X = 4

funcs = [ "swap_polygons", "rotate", "flip", "add_vertex" ]

for i in range(3):
   
    # Original figure
    XX = int(random.random()*10) + 3
    A = Polygon(no_of_sides = XX)
    A.makeRandomCircumcircle()
    polys = [A]
    
    plt.figure()

    for j in range(2):
        # plt.figure()
        XX = int(random.random()*10) + 3
        XX = int(random.random())+3
        print(XX,"isXX")
        B = Polygon(no_of_sides = XX, size= random.random()*40 )
        B.clone_circumcircle(A)
            # Center remains same as A but the radius can be anything less than A's raduis
        B.circumcircle.radius = 0.8 * B.circumcircle.radius
        B.makeShape()
        # B.drawPolygon()
        polys.append(B)
        A = B

    for pl in polys:
        pl.drawPolygon()

    plt.axis('image')
    plt.axis('off')
    plt.savefig("./plot/seq/plot"+str(i)+"original_.png")

    


    # Original transform
    func_names = []
    params = []
    plt.figure()

    for k ,pl in enumerate(polys):

        func_name = funcs[int(random.random()*len(funcs))]
        func_names.append(func_name)

        func_call = getattr(pl,func_name)

        if func_name == 'swap_polygons':
            index = i-1 if i>0 else i+1
            otherpoly = polys[index]
            print("swap with",index)
            params.append(index)
            func_call(otherpoly)
        elif func_name == 'rotate':
            theta = rndangle()
            params.append(theta)
            print("rotate by",theta)
            func_call(theta)
        else:
            params.append('')


    for pl in polys:
        pl.drawPolygon()

    plt.axis('image')
    plt.axis('off')
    plt.savefig("./plot/seq/plot"+str(i)+"originaltransform_.png")



    
    # Second figure
    XX = int(random.random()*10) + 3
    A = Polygon(no_of_sides = XX)
    A.makeRandomCircumcircle()
    polys = [A]
    
    plt.figure()

    for j in range(2):
        # plt.figure()
        XX = int(random.random()*10) + 3
        XX = int(random.random())+3
        print(XX,"isXX")
        B = Polygon(no_of_sides = XX, size= random.random()*40 )
        B.clone_circumcircle(A)
            # Center remains same as A but the radius can be anything less than A's raduis
        B.circumcircle.radius = 0.8 * B.circumcircle.radius
        B.makeShape()
        # B.drawPolygon()
        polys.append(B)
        A = B

    for pl in polys:
        pl.drawPolygon()

    plt.axis('image')
    plt.axis('off')
    plt.savefig("./plot/seq/plot"+str(i)+"copy.png")


    # Second figure transform
    plt.figure()


    for k ,pl in enumerate(polys):
        print("k is",k)
        func_name = func_names[k]
        func_call = getattr(pl,func_name)

        if func_name == 'swap_polygons':
            index = params[k]
            otherpoly = polys[k]
            print("swap with",index)
            func_call(otherpoly)
        elif func_name == 'rotate':
            theta = params[k]
            print("rotate by",theta)
            func_call(theta)

    for pl in polys:
        pl.drawPolygon()

    plt.axis('image')
    plt.axis('off')
    plt.savefig("./plot/seq/plot"+str(i)+"copytransform_.png")





