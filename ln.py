from graphics import *
import vec, pt, random

v = vec.vector(250,250,90,100)
p = pt.point(100,100)
def main():
	win = GraphWin("Line", 500, 500)
	p.draw(win)
	input("press enter to start")
	for x in range (0, 100):
		global v 
		v = test(v,p,win)
	win.getMouse()
	win.close()

def test(vector,point,window):
	angle = vector.t
	length = vector.l
	holdv = vector
	for x in range(0,100):	
		aadd = random.random() * 10
		ladd = random.random() * 10
		if (random.random() < .5):
			aadd = -aadd
		if (random.random() < .5):
			ladd = -ladd
		testv = vec.vector(vector.x,vector.y,angle+aadd,length+ladd)
		#testv.draw(window)
		#print(point.getd(testv))
		if (point.getd(testv) < point.getd(holdv)):
			holdv = testv
			holdv.draw(window)
			print("more efficient pathway found")
			print("angle: " + str(holdv.t))
			print("length: " + str(holdv.l))
			print("distance: " + str(point.getd(holdv)))

	return holdv
		

main()
