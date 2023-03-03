from graphics import*
import random

def fourcorners():
    win = GraphWin("Four Corners", 400, 400)
    s1 = Rectangle(Point(0,0), Point(100, 100))
    s1.draw(win)
    s2 = Rectangle(Point(300,0), Point(400, 100))
    s2.draw(win)
    s3 = Rectangle(Point(0,300), Point(100, 400))
    s3.draw(win)
    s4 = Rectangle(Point(300,300), Point(400, 400))
    s4.draw(win)


def generatePhoneNumber():
    win2 = GraphWin("Generate Phone Numbers", 500, 400)
    E1 = Entry(Point(250,200), 10)
    E1.draw(win2)
    T = Text(Point(250, 300), "")
    T.draw(win2)
    listsnum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:

        num = E1.getText()
        num1 = list(num)



                    

        for i in range(7):
        
            num1.append(random.choice(listsnum))
                
                
        T.setText(num1)


    




        


def main():
    fourcorners()
    generatePhoneNumber()
    
    





if __name__=="__main__":
    main()
