from Button import*
from graphics import*
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
        self.color=""
        self.xCoord=x
        self.yCoord=y
        self.lines=[]
        

    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def setColor(self, c):
        self.color=c
        self.C.setFill(c)

    def getColor(self):
        return self.color

    def getDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name

    def addLine(self,l):
        self.lines.append(l)

class Graph:

    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
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
                name = "# "+str(numN+1)#names[numN]
                N = Node(x, y, win, name)
                self.nodes.append(N)
                #self.numCoord.update({name:[x,y]})
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
            node.setColor("white")

    def getNumCoord(self):
        return self.numCoord

    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

    def getAllDegrees(self):
        d={}
        for n in self.nodes:
            print(str(n.getDegree()) + " : " + n.getName())

    def makeDict(self):
        self.allNodes={}
        for n in self.nodes:
            self.allNodes[n.getName()]=n.getDegree()
        return(self.allNodes)

    def nameList(self):
        self.allNodes=self.makeDict()
        self.name = list(self.allNodes.keys())
        return(self.name)

    def degreeList(self):
        self.allNodes=self.makeDict()
        self.degree = list(self.allNodes.values())
        return(self.degree)
    
    def maxDegree(self):
        self.keys = self.nameList()
        self.values = self.degreeList()
        self.maxi = max(self.values)
        self.index=[]

        for i in range(len(self.values)):
            if self.values[i] == self.maxi:
                self.index.append(i)     
        for i in self.index:
            self.name=self.keys[i]
            print(str(self.name)+" has the greatest degree of "+str(self.maxi))
            
        return(self.maxi)

    def minDegree(self):
        self.keys = self.nameList()
        self.values = self.degreeList()
        self.mini = min(self.values)
        self.index=[]

        for i in range(len(self.values)):
            if self.values[i] == self.mini:
                self.index.append(i)   
        for i in self.index:
            self.name=self.keys[i]
            print(str(self.name)+" has the smallest degree of "+str(self.mini))

        return(self.mini)

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
                

    def removeNode(self,win):
        r=30
    
        m=win.getMouse()
        x=m.getX()
        y=m.getY()
        xCoordinates=[]
        yCoordinates=[]
        coordinates=[]
        
        for node in self.nodes:
            xCoordinates.append(node.xCoord)
            yCoordinates.append(node.yCoord)
            coordinates.append((node.xCoord,node.yCoord))
        
        for i in range(len(coordinates)):
            if (x-coordinates[i][0])**2+(y-coordinates[i][1])**2<=r**2:
                self.nodes[i].undraw()
                node=self.nodes[i]
                #remove the node from the neighbors
                for n in self.nodes:
                    l=n.getNeighbors()
                    if node in l:
                        l.remove(node)
                self.nodes.remove(self.nodes[i])
        
                for a in coordinates:
                    edgeCoordX1=int(coordinates[i][0])
                
                    for c in self.E:
                        if (c.getP1()).getX()==edgeCoordX1 or (c.getP2()).getX()==edgeCoordX1: 
                           c.undraw()

    def addEdge(self,win):
        r=30
        self.xCoordinates=[]
        self.yCoordinates=[]
        self.coordinates=[]
        
        for node in self.nodes:
            self.xCoordinates.append(node.xCoord)
            self.yCoordinates.append(node.yCoord)
            self.coordinates.append((node.xCoord,node.yCoord))
            
        l=[]
        n=[]
        while True:
            m=win.getMouse()
            x=m.getX()
            y=m.getY()
            l.append(x)
            l.append(y)
    
            if len(l)>4:
                print("cicked more than 2")
                break

            if len(l)==4:

                for node in self.nodes:
                    if (node.xCoord-l[0])**2+(node.yCoord-l[1])**2<=r**2 or (node.xCoord-l[2])**2+(node.yCoord-l[3])**2<=r**2:
                        n.append(node)
                        
                if len(n)<2:
                    print("didn't click nodes")
                    break
                
                node1=n[0]
                node2=n[1]

                if node2 in node1.getNeighbors():
                    print("already connected")
                    break

                edge=Line(Point(node1.xCoord,node1.yCoord),Point(node2.xCoord,node2.yCoord))
                self.E.append(edge)
                edge.draw(win)
                node1.addNeighbor(node2)
                node2.addNeighbor(node1)
                break
            
    def coloring(self):

        maxNeighbors=0

        for n in self.nodes:
            if len(n.getNeighbors())>maxNeighbors:
                maxNeighbors=len(n.getNeighbors())

        for node in self.nodes:
            nodeColor=node.getColor()
            unavailableColor=[]
            self.colorList=["darkorchid","lightgoldenrod1","orchid","white","grey", "brown"]

            if maxNeighbors>len(self.colorList):
                self.colorList=self.colorList
            else:

                for i in range(len(self.colorList)-(maxNeighbors+1),0):
                    self.colorList.remove(self.colorList[i])

            for neighbor in node.getNeighbors():
                unavailableColor.append(neighbor.getColor())
                #print(neighbor.getColor())
                #if neighbor.getColor()==nodeColor:
                 #   unavailableColor.append(neighbor.getColor())
                    
            for c in unavailableColor:
                if c in self.colorList:
                    #print(unavailableColor)
                    self.colorList.remove(c)

            if len(self.colorList)<= 0:
                true=True

            else:
                    
                if len(self.colorList)-1<0:
                    r=0
                else:
                    r=len(self.colorList)-1
                #print(node.getName() ,self.colorList)


                newColor=self.colorList[random.randint(0,r)]
                node.setColor(newColor)
                for node1 in self.nodes:
                    if node in node1.getNeighbors():
                        node.setColor(newColor)
            
        
                
            
            '''
            for neighbor in self.neighborsList:
                self.colorList=["darkorchid","lightgoldenrod1","orchid","white"]
                self.colorList.remove(nodeColor)
                if neighbor.getColor()==nodeColor:
                    neighbor.setColor(self.colorList[random.randint(0,len(self.colorList)-1)])
            '''
    def getUserNode(self,win):
        E1=Entry(Point(100,330),20)
        E1.draw(win)
        return E1
    def getUserEdge(self,win):
        E2=Entry(Point(100,380),20)
        E2.draw(win)
        return E2
        
        
def main():

    win = GraphWin("Graph Example", 800, 600)
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    NodeSubmit=Button(win,Point(30,345),Point(170,360),"tomato","submit number of nodes")
    EdgeSubmit=Button(win,Point(30,395),Point(170,410),"tomato","submit number of edges")
    RemoveNode=Button(win,Point(120,430),Point(230,490),"cyan","Remove Node")
    addEdge=Button(win,Point(120,530),Point(230,590),"cyan","Add Edge")
    maxDegree=Button(win,Point(30,270),Point(150,300),"Cyan","Greatest Degree")
    minDegree=Button(win,Point(30,230),Point(150,260),"Cyan","Smallest Degree")
    hasCycle=Button(win,Point(30,190),Point(150,220),"Cyan","Has Cycle")
    G = Graph(1, 0, win)


    while True:
        E1=G.getUserNode(win)
        E2=G.getUserEdge(win)
        m = win.getMouse()
        if Q.isClicked(m):
            break
        
        if NodeSubmit.isClicked(m):
            nodeNum=E1.getText()
            print("Number of nodes: ",nodeNum)

        if EdgeSubmit.isClicked(m):
            edgeNum=E2.getText()
            print("Number of edges: ",edgeNum)

        if RemoveNode.isClicked(m):
             G.removeNode(win)
             G.coloring()

        if addEdge.isClicked(m):
            G.addEdge(win)
            G.coloring()

        if maxDegree.isClicked(m):
            G.maxDegree()

        if minDegree.isClicked(m):
            G.minDegree()

        if hasCycle.isClicked(m):
            print(G.hasCycle())
            
        
        if Gen.isClicked(m):
            G.delete()
            #Create a graph with (num Nodes, num Edges)
            #print(nodeNum)
            G = Graph(int(nodeNum),int(edgeNum), win)
            G.coloring()

        
    win.close()


if __name__ == "__main__":
    main()
