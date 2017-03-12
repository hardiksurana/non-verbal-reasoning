# Pythons math library (math.sin, math.cos) works with radians
# All angles in this project are radians 
# All angles are measured from the X-axis anti-clockwise


import random, math
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt


CANVAS_SIZE = 10

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
		self.circumcircle = None

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
		# print "Random Circumcircle",self.circumcircle

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
			# print(self," is Regular")
			# Then theta is incremented uniformly by 360/N
			angle_increment = 2*math.pi / self.N

			# print("Angle of increment", angle_increment)
			
			# Add points
			for i in range(self.N):
				# print(start_angle + i*angle_increment)
				cur_angle = start_angle + i*angle_increment
				self.point_angles.append(cur_angle)
				self.points.append(getpoints(self.circumcircle.radius, cur_angle,
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
				cur_angle = i*angle_increment[i%len(angle_increment)]
				self.point_angles.append(cur_angle)
				self.points.append( getpoints(self.circumcircle.radius, cur_angle, self.circumcircle.x, self.circumcircle.y ) )


	def drawPolygon(self):
		points = self.points
		# fill = True if random.random() < 0.5 else False
		fill=False
		polygon = plt.Polygon(points,fill=fill)
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
		Generate this object inside the otherpoly
	'''
	def gen_inside(self,otherpoly):
		self.circumcircle = Circumcircle(otherpoly.circumcircle.radius / 2 , otherpoly.circumcircle.x, otherpoly.circumcircle.y )
		self.makeShape()

	def rotate(self,theta):
		# rotate the current polygon clockwise by theta
		self.points = []
		
		# Find new points drawn at new angles.
		for cur_angle in self.point_angles:
			self.points.append(getpoints(self.circumcircle.radius, cur_angle + theta,
											 self.circumcircle.x, self.circumcircle.y))

		# Update the angles ate which vertices are drawn
		self.point_angles = [ cur_angle + theta for cur_angle in self.point_angles]
		pass

	def add_vertex(self):
		# Add a random vertex to the figure 
		self.N += 1
		self.makeShape()
		
	def delete_vertex(self):
		self.N -= 1
		if self.N <= 3:
			# Can't do nothing
			raise "Error: Polygon can't exist with less than 3 vertices "
			pass
		else:
			self.N -= 1  
			self.makeShape()

	"""
	Change the circumcircle for the Polygon 
	"""
	def clone_circumcircle(self,otherpoly):
		self.circumcircle = Circumcircle(otherpoly.circumcircle.radius,otherpoly.circumcircle.x,otherpoly.circumcircle.y)
		self.makeShape()
	
	"""
	Flip the image
	how : vert - about vertical axis
		  hori - about horizontal axis 
	"""
	def flip(self,how='vert'):
		pts = []
		if how == 'vert':
			for pt in self.points:
				x,y = pt
				xdist = self.circumcircle.x - x

				x,y = 2 * self.circumcircle.x - x, y
				pts.append((x,y))
		elif how == 'hori':
			print "hori"
			for pt in self.points:
				x,y = pt
				x,y = x, 2* self.circumcircle.y - y
				pts.append((x,y))
		# Update the points
		self.points = pts

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

	# plt.figure()
	# A = Polygon(no_of_sides=5,isRegular=True)
	# A.makeRandom()
	# A.makeShape()
	# print A,"giri"
	# print A.points
	# A.drawPolygon()
	# # A.flip()
	# # A.drawPolygon(	)
	# A.flip(how='hori')
	# A.drawPolygon()
	# # plt.show()
	# plt.axis('image')
	# plt.savefig('./test.png')

	# for l in range(10):
	# 	import matplotlib.pyplot as plt
	# 	#Cleans canvas starts a new figure 
	# 	plt.figure()
	# 	A = Polygon(	)
	# 	A.makeRandom()
	# 	print("Original radius",A.circumcircle.radius)
	# 	A.drawPolygon()
	# 	radius = A.circumcircle.radius
	# 	centerx = A.circumcircle.x
	# 	centery = A.circumcircle.y

	# 	# for i in range(int(random.random()*8)):

	# 	for j in range(5):
	# 		B = Polygon(no_of_sides=int(random.random() * 10)+3)
	# 		# same center and radiu
	# 		B.clone_circumcircle(A)
	# 		new_radius = random.random() * B.circumcircle.radius
	# 		print("New radius",new_radius)
	# 		B.circumcircle.radius = new_radius
	# 		B.makeShape()
	# 		# otherpoly = Polygon(no_of_sides=int(random.random()*20) + 3)
	# 		# otherpoly.clone_circumcircle(B)
	# 		B.drawPolygon()
	# 			# A = B
	# 	# plt.axis('equal')
	# 	plt.axis('image')
	# 	# plt.axis('tight')
	# 	plt.axis('off')
	# 	plt.savefig('./plot/plot'+str(l)+'.png')
		# raw_input()
	print "END"


