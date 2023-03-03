from Button import*
import random
import time

class Node:
    def __init__(self, x, y, win):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []

    def draw(self, win):
        self.C.draw(win)

    def undraw(self):
        self.C.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

    def getDegree(self):
        return len(self.neighbors)

    def maxDegree(self):
        count = 0
        for n in getNeighbors:
            deg = len(n.getNeighbors())
            if deg > count:
                count = deg
        return count
    def minDegree(self):
        count = 25
        for n in getNeighbors:
            deg = len(n.getNeighbors())
            if deg < count:
                count = deg
        return count
        


class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                N = Node(x, y, win)
                self.nodes.append(N)
                numN += 1

            if numN == n:
                break

        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)

        for node in self.nodes:
            node.draw(win)
            node.color("white")

    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()
        
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Gen.isClicked(m):
            G.delete()
            G = Graph(7, 10, win)
    

    print("Max degree: ", maxDegree())
    print("Min degree: ", minDegree())
    win.close()

if __name__ == "__main__":
    main()
