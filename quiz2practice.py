from graphics import*
from Button import*

# Define different methods to answer a question / solve a probem
# create a circle inscribed within a square at least 100px wide
def problem1():
    win = GraphWin("SquareCircle", 500, 400)
    # Graphwin is to create a graphic with the first element is the name, second is the width, and third is the length
    S = Rectangle(Point(1,1),Point(201,201))
    # Rectangle command takes in first element is the top left point, and second is the bottom right point of the rectangle - point(x,y).
    S.draw(win)
    C = Circle(Point(101, 101), 100)
    # Circle command takes in the first element is the center of the circle point(x, y), and second is the radius
    C.draw(win)

# Create a GUI which gets two user inputs as interger
# Displace them in Text if they are the same number
def problem2():
    win2 = GraphWin("Problem 2", 500, 400)
    T = Text(Point(200, 100), "")
    T.draw(win2)
    E1 = Entry(Point(100, 300), 20)
    E1.draw(win2)
    E2 = Entry(Point(300, 300), 20)
    E2.draw(win2)
    while True:
        num1 = E1.getText()
        num2 = E2.getText()
        if num1 == num2:
            T.setText("They are the same!")
        else:
            T.setText("They are not the same")

# Create GUI which gets one user input as an intergers and draws a circle with that radius
def problem3():
    win3 = GraphWin("Problem3", 500, 400)

    E1 = Entry(Point(100, 300), 20)
    E1.draw(win3)
    E1.setText("0")

    while True:
        num1 = E1.getText()
        r = int(num1)
        C = Circle(Point(200, 200), r)
        C.draw(win3)

# Creat GUI which get two string as input and tests if they are
# Anagrams of each other (Anagrams are "scrambled" letters of eachother
def problem4():
    win4 = GraphWin("Prolem4", 500, 400)
    T = Text(Point(200, 100), "")
    T.draw(win4)
    E1 = Entry(Point(100, 300), 20)
    E1.draw(win4)
    E2 = Entry(Point(300, 300), 20)
    E2.draw(win4)
    while True:
        
        str1 = E1.getText()
        str2 = E2.getText()


            
        l1 = list(str1)
        l2 = list(str2)
        an = True
        for c in l1:
            if c in l2:
                l2.remove(c)
            else:
                an = False
        T.setText("We have an anagram: " + str(an))
        
        '''
        if str1 == str2:
            T.setText("They are the same!")
        else:
            T.setText("They are not the same")'''

#Create a GUI which draws a table with 3 columns and 5 rows
# columns should be equal width
# rows should be equal length
def problem5():
    win5 = GraphWin("Problem 5", 500, 400)

    


    V2 = Line(Point(500/3, 0), Point(500/3, 400))
    V2.draw(win5)
    V3 = Line(Point(500/3*2, 0), Point(500/3*2, 400))
    V3.draw(win5)

    H = Line(Point(0, 0), Point(500, 0))
    H.draw(win5)
    H2 = Line(Point(0, 400/5), Point(500, 400/5))
    H2.draw(win5)
    H3 = Line(Point(0, 400/5*2), Point(500, 400/5*2))
    H3.draw(win5)
    H4 = Line(Point(0, 400/5*3), Point(500, 400/5*3))
    H4.draw(win5)
    H5 = Line(Point(0, 400/5*4), Point(500, 400/5*4))
    H5.draw(win5)
    
    


# Create a GUI with a 'target' (A circle wth 3 sections)
# if the user clicks within the target. The texts updates and says 'hit'
# if the user clicks outside the target the next updates and says 'miss'
def problem6():
    win6 = GraphWin("Target", 500, 400)
    C = Circle(Point(250, 200), 50)
    C.draw(win6)
    T = Text(Point(250, 100), "")
    T.draw(win6)

    while True:
        p = win6.getMouse()
        x = p.getX()
        y = p.getY()
        center = C.getCenter()
        x2 = center.getX()
        y2 = center.getY()
        deltaX = x2 - x
        deltaY = y2 - y
        distanceSquared = deltaX*deltaX + deltaY*deltaY
        if 50*50 >= distanceSquared:
            T.setText("hit")
        else:
            T.setText("miss")

        
    
    

    

def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #problem5()
    problem6()



if __name__=="__main__":
    main()
