from graphics import *
from Button import *
import time

def spin(r, win):
    points = r.getPoints()
    p1, p2, p3, p4 = points[0], points[1], points[2], points[3]
    
    p1 = Point(p1.getX() + 50, p1.getY() - 50)
    p2 = Point(p2.getX() + 50, p2.getY() + 50)
    p3 = Point(p3.getX() - 50, p3.getY() + 50)
    p4 = Point(p4.getX() - 50, p4.getY() - 50)
    print(p1, p2, p3, p4)
    r.undraw()
    r = Polygon([p1, p2, p3, p4])
    r.draw(win)
    return r
    
    

def main():

    win = GraphWin("Spin", 800, 600)

    R = Polygon([Point(400, 300), Point(500, 300), Point(500, 400), Point(400, 400)])
    R.draw(win)

    for i in range(10):
        time.sleep(.5)
        R = spin(R, win)

if __name__ == "__main__":
    main()
