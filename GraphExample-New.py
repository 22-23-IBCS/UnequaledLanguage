from Button import*
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)

    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)

    def calcDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def removeNeighbor(self, node):
        self.neighbors.remove(node)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

    def printNeighbors(self):
        l = []
        for n in self.neighbors:
            l.append(n.getName())
        return l

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
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
                name = self.names.pop(0)
                N = Node(x, y, win, name)
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
            #print(str(node.calcDegree()) + " : " + node.getName())
            
    def addNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        name = self.names.pop(0)
        N = Node(x, y, win, name)
        neighbor = random.choice(self.nodes)
        N.addNeighbor(neighbor)
        neighbor.addNeighbor(N)
        self.nodes.append(N)
        L = Line(Point(x, y), neighbor.getCenter())
        L.draw(win)
        self.E.append(L)
        neighbor.undraw()
        neighbor.draw(win)
        N.draw(win)
        N.color("white")

    def removeNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        saved_node = 0
        for node in self.nodes:
            if (node.center.getX() - x)*(node.center.getX() - x) + (node.center.getY() - y)*(node.center.getY() - y) < 900:
                saved_node = node
                break

        if saved_node != 0:
            saved_node.undraw()
            for neighbour in node.getNeighbors():
                neighbour.removeNeighbor(saved_node)
            deletion_list = []
            for line in self.E:
                if (line.getP1().getX() == saved_node.center.x and line.getP1().getY() == saved_node.center.getY()) or (line.getP2().getX() == saved_node.center.getX() and line.getP2().getY() == saved_node.center.getY()):
                    line.undraw()
                    deletion_list.append(line)
            for edge in deletion_list:
                self.E.remove(edge)
            self.nodes.remove(saved_node)

    def addEdge(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        saved_node1 = 0
        for node in self.nodes:
            if (node.center.getX() - x)*(node.center.getX() - x) + (node.center.getY() - y)*(node.center.getY() - y) < 900:
                saved_node1 = node
                break

        if saved_node1 == 0:
            return

        m = win.getMouse()
        x = m.getX()
        y = m.getY()

        saved_node2 = 0
        for node in self.nodes:
            if (node.center.getX() - x)*(node.center.getX() - x) + (node.center.getY() - y)*(node.center.getY() - y) < 900:
                saved_node2 = node
                break

        if saved_node2 == 0 or saved_node1 == saved_node2:
            return

        for line in self.E:
            if (line.getP1().getX() == saved_node1.center.x and line.getP1().getY() == saved_node1.center.getY()) and (line.getP2().getX() == saved_node2.center.getX() and line.getP2().getY() == saved_node2.center.getY()):
                return
            if (line.getP1().getX() == saved_node2.center.x and line.getP1().getY() == saved_node2.center.getY()) and (line.getP2().getX() == saved_node1.center.getX() and line.getP2().getY() == saved_node1.center.getY()):
                return
            
        L = Line(saved_node1.center, saved_node2.center)
        saved_node1.undraw()
        saved_node2.undraw()
        L.draw(win)
        saved_node1.draw(win)
        saved_node2.draw(win)
        self.E.append(L)
        
    
    def minDegree(self):
        minD = 100
        for node in self.nodes:
            if node.calcDegree() < minD:
                minD = node.calcDegree()
        return minD

    def maxDegree(self):
        maxD = 0
        for node in self.nodes:
            if node.calcDegree() > maxD:
                maxD = node.calcDegree()
        return maxD
    
    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

    def hasCycle(self):
        for n in self.nodes:
            #call traverse graph (recursive function) on each node in the graph
            #if it is every true (cycle found) return true.
            if self.traverseGraph(n, n, []):
                return True
        # if it never returned true, there was never a cycle
        return False
                        
    def traverseGraph(self, current, previous, visited):
        #base case -- dead end
        if len(current.getNeighbors()) <= 1:
            return False

        #see possible neighbors to still visit
        check = []
        for node in current.getNeighbors():
            # return true if one of the neighbors has been previously visited
            if (node in visited) and (node != previous):
                return True
            #otherwise, add unvisited nodes to a list to traverse
            elif node != previous:
                check.append(node)
                
        #update visited nodes  
        visited.append(previous)
        for node in check:
            #recursive call on each new unvisited neighbor
            if self.traverseGraph(node, current, visited):
                return True
        return False
                
        
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    #buttons
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    AddNode = Button(win, Point(20, 330), Point(100, 390), "beige", "Add Node")
    Degrees = Button(win, Point(20, 230), Point(100, 290), "beige", "Calc Degrees")
    Cycle = Button(win, Point(20, 130), Point(100, 190), "beige", "Has Cycle?")
    DeleteNode = Button(win, Point(20, 30), Point(100, 90), "beige", "Delete Note")
    AddEdge = Button(win, Point(120, 30), Point(220, 90), "beige", "Add Edge")
    
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Degrees.isClicked(m):
            print("Minimum Degree: " + str(G.minDegree()))
            print("Maximum Degree: " + str(G.maxDegree()))
        if Cycle.isClicked(m):
            if G.hasCycle():
                print("The graph has a cycle")
            else:
                print("The graph does not have a cycle")
        if Gen.isClicked(m):
            print("\n===================================\n")
            G.delete()
            #GRaph made with number of nodes and number of edges
            G = Graph(5, 4, win)
        if AddNode.isClicked(m):
            G.addNode(win)
        if DeleteNode.isClicked(m):
            G.removeNode(win)
        if AddEdge.isClicked(m):
            G.addEdge(win)
            
    win.close()

if __name__ == "__main__":
    main()
