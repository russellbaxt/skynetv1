from graphics import *
import math

class vector:
	def __init__(self, x, y, t, l):
		self.x = x
		self.y = y
		self.t = t
		self.l = l
		self.a = self.calca(l,t)
		self.b = self.calcb(l,t)

	def draw(self,win):
		p=Point(self.x,self.y)
		c=Circle(p,4)
		c.setFill('black')
		p.draw(win)	
		c.draw(win)

		ln = Line(p, Point(self.x-self.a, self.y-self.b))
		ln.draw(win)

	def calca(self,l,t):
		a = l * math.cos(t*math.pi/180)
		return a
		
	def calcb(self,l,t):
		b = l * math.sin(t*math.pi/180)
		return b
		
		
