from graphics import *
import vec, math

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getd(self, vec):
		h = (((self.x-(vec.x-vec.a))**2 + (self.y-(vec.y-vec.b))**2)**.5)
		#print(h)
		return(h)

	def draw(self, win):
		p = Point(self.x,self.y)
		c = Circle(p,4)
		p.draw(win)
		c.setFill('black')
		c.draw(win)
