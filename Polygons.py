# Pythons math library (math.sin, math.cos) works with radians
# All angles in this project are radians 
# All angles are measured from the X-axis anti-clockwise

# Currently, we plan to use only 

import random, math
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


CANVAS_SIZE = 100

def rnd(zeroToOne=0):
    # if zeroToOne is 1, returns a number between 0 and 1 (inclusive)
    # else returns a number between -1 and 1 (inclusive)

    if zeroToOne == 1:
        return random.random()
    else:
    
        if round(random.random()) == round(0):
            # id generated number between 0 and 0.5
            return random.random()    
        else:
            return random.random() * -1

def rndangle():
    # return a random angle [in radians] between 0 and 360 deg
    return rnd(1) * 2*math.pi

def getpoints(R,theta,Xcenter,Ycenter):
    # finds the new points on circle, with radius R, center (Xcenter,Ycenter), at an angle theta
    return ( (Xcenter + (R*math.cos(theta)) ), (Ycenter + (R*math.sin(theta)) ) )


# Circumcirle - has a radius and a x,y co-ordinates for the center
class Circumcircle:
    def __init__(self,size,centerx,centery):
        self.radius = size
        self.x = centerx
        self.y = centery

    def __repr__(self):
        return "Circumcircle: radius %s, Center: (%s,%s)" % (self.radius, self.x,self.y)

# Represents a shape 
class Polygon : 
    
    def __init__(self, no_of_sides=4,size=30,isRegular=True):
        # size is for the circumcircle radius    
        self.size = size
        self.N = no_of_sides
        self.isRegular = isRegular
        self.points = []

        # The angles at which each point was drawn 
        # This will be helpful in case of rotating and other things(I can't think of right now.)
        self.point_angles = []

    '''
        This shape is drawn randomly
        considering this as the first shape to be drawn

        makeRandom: makes a Circumcircle with random Center
    '''
    def makeRandom(self):    
        # The shape is randomly drawn
        # Step1 : Make the circumcircle randomly

        # generate center points between 0 and 100
        self.circumcircle = Circumcircle(self.size, round(rnd(zeroToOne=1)*CANVAS_SIZE), round(rnd(zeroToOne=1) *
                                                                                               CANVAS_SIZE))

        print "Random Circumcircle",self.circumcircle
        
        # Step2 :  Then call makeShape()
        self.makeShape()


    """
    Given a Circumcircle and No_of_points generate points for the 
    polygon
    """
    def makeShape(self):
        # Uses the information - circumcircle(radius,x,y) + no_of_sides + isRegular to generate vertices
        # for the polygon

        # Start with empty lists of points 
        self.points = []
        
        # Pick a random angle 
        start_angle = rndangle()

        if self.isRegular:
            print(self," is Regular")
            # Then theta is incremented uniformly by 360/N
            angle_increment = 2*math.pi / self.N

            print("Angle of increment", angle_increment)
            
            # Add points
            for i in range(self.N):
                print(start_angle + i*angle_increment)
                self.points.append(getpoints(self.circumcircle.radius, start_angle + i*angle_increment,
                                             self.circumcircle.x, self.circumcircle.y))

        else:
            # Then theta is incremented by randangle 
            # NOTE: A minimum value should be defined for increment,
            # otherwise the generated points would be too close to 
            # each other
            # NOTE: We need to be sure that all points are unique!!
            
            # Currently increment with one of the values in angle_increment
            angle_increment = [2*math.pi / 12, 2*math.pi / 6 ,2*math.pi / 18]
            
             # Add points
            for i in range(self.N):
                self.points.append( getpoints(self.circumcircle.radius, start_angle + i*angle_increment[i%len(angle_increment)], self.circumcircle.x, self.circumcircle.y ) )


    def drawPolygon(self):
        points = self.points
        polygon = plt.Polygon(points)
        plt.gca().add_patch(polygon)

    def drawCircle(self):
        circle = plt.Circle((self.circumcircle.x, self.circumcircle.y), self.circumcircle.radius, fc='y')
        plt.gca().add_patch(circle)
    
    '''
        Generate this object outside the poly
    '''
    def gen_outside(self,otherpoly):
        # otherpoly should be a polygon
        if not type(otherpoly) == type(self):
            # raise error
            print("Something is wrong: Wrong type"+type(self))
        else:

            total_distance  = otherpoly.circumcircle.radius + self.size # +some_random_distance

            # Get a random angle to draw the new image
            draw_angle = rndangle()

            self_center = getpoints( total_distance, draw_angle, otherpoly.circumcircle.x, otherpoly.circumcircle.y )
            self.circumcircle = Circumcircle( self.size, self_center[0], self_center[1])

            # Genereate points for otherpoly
            self.makeShape()

    
    '''
        Generate this object outside the poly
    '''
    def gen_outside_all(self, *otherpolys):

        for i in otherpolys:
            assert (type(i) == type(self))

        common_center_x = sum([poly.circumcircle.x for poly in otherpolys]) / len(otherpolys)
        common_center_y = sum([poly.circumcircle.y for poly in otherpolys]) / len(otherpolys)
        distance = self.size + sum([poly.size for poly in otherpolys])

        # Get a random angle to draw the new image
        draw_angle = rndangle()

        self_center = getpoints( distance, draw_angle, common_center_x, common_center_y )
        self.circumcircle = Circumcircle( self.size, self_center[0], self_center[1])

        # Genereate points for otherpoly
        self.makeShape()

    
    '''
        Generate this object inside the poly
    '''
    def gen_inside(self,otherpoly):
        self.circumcircle = Circumcircle(otherpoly.circumcircle.radius / 2 , otherpoly.circumcircle.x, otherpoly.circumcircle.y )
        self.makeShape()

    def rotate(self,theta):
        # rotate the current polygon clockwise by theta
        pass

    def add_vertex(self):
        # Add a random vertex to the figure 

        pass
    def delete_vertex(self):
        # Delete a vertex from the figure 

    def is_inside(self,otherpoly):
        pass













        # otherpoly should be a polygon
        # if not type(*otherpolys) == type(self):
        #     # raise error
        #     print("Something is wrong: Wrong type" + type(self))
        # else:
        #
        #     total_distance = self.circumcircle.radius + otherpoly.size  # +some_random_distance
        #
        #     # Get a random angle to draw the new image
        #     draw_angle = rndangle()
        #
        #     otherpoly_center = getpoints(total_distance, draw_angle, self.circumcircle.x, self.circumcircle.y)
        #     otherpoly.circumcircle = Circumcircle(otherpoly.size, otherpoly_center[0], otherpoly_center[1])
        #
        #     # Genereate points for otherpoly
        #     otherpoly.makeShape()





                    # Define the circumcircle for the new shape


            # 1. get self's circumcircle
            # 2. Distance for the centre is self.size + other.size(+ some Random offset)
            # Random offset is added to make the diagram more random-looking, even though 
            # the information about the scale of how images are drawn is not considered 
            # (except for some trivial case - smale/large etc)
            # 3.






    # def gen_outside
        # returns a polugon completely outside

    # def gen_inside 
    # returns a polygon completely inside

    def __repr__(self):
        return "Polygon: %s sides, circumcircle: %s" % (self.N,self.circumcircle)

if __name__ == '__main__':
    A = Polygon(no_of_sides=5)
    B = Polygon(size=30)
    C = Polygon(no_of_sides=6)
    D = Polygon(no_of_sides=3)
    E = Polygon(no_of_sides=7)
    plt.axes(xlim=(0, 500), ylim=(0, 500))


    # draw A anywhere
    A.makeRandom()
    A.drawCircle()
    A.drawPolygon()


    # draw B outside A
    B.gen_outside(A)
    B.drawCircle()
    B.drawPolygon()

    C.gen_outside_all(A, B)


    # B.gen_outside(C)
    C.drawCircle()
    C.drawPolygon()


    D.gen_inside(A)


    # B.gen_outside(C)
    D.drawCircle()
    D.drawPolygon()



    E.gen_inside(D)


    # B.gen_outside(C)
    E.drawCircle()
    E.drawPolygon()

    # print A,A.points
    # print B,B.points



    # plt.axis('scaled')

    plt.show()

    # import turtle

    # turtle.setup(800, 600)      # set the window size to 800 by 600 pixels
    # wn = turtle.Screen()        # set wn to the window object
    # wn.bgcolor("lightgreen")    # set the window background color
    # wn.title("Hello, Tess!")    # set the window title

    # sq = [(0,0),(0,10),(10,0),(10,10)]

    # poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
    # s = turtle.Shape("compound")
    # s.addcomponent(poly1, "red", "blue")
    # wn.register_shape("ss",s)
    # turtle.shape("ss")

    # wn.exitonclick()
    print "END"


