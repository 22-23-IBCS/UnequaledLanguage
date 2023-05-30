from graphics import*
from Button import*
import math
def main():
    win = GraphWin("Badminton Stats Analysis", 520, 380)
    T = Text(Point(50, 10), "")
    T.draw(win)
    T.setText("Information")

    Q = QuitButton(win, Point(300, 250), Point(380, 270))
    B1 = Button(win, Point(300, 180), Point(380, 200), "Blue", "Confirm Data")
    B2 = Button(win, Point(300, 215), Point(380, 235), "Blue", "Create Graph")
    

    T1 = Text(Point(100, 40), "")
    T1.draw(win)
    T1.setText("Opponent Name:")

    E1 = Entry(Point(200.5, 40), 10)
    E1.draw(win)

    T2 = Text(Point(50, 100), "")
    T2.draw(win)
    T2.setText("Stats")

    T3 = Text(Point(200, 130), "")
    T3.draw(win)
    T3.setText("High Serve Success Rate")

    E2 = Entry(Point(170, 155), 5)
    E2.draw(win)
    E2.setText("")
    T4 = Text(Point(200, 155), "")
    T4.draw(win)
    T4.setText("/")
    E3 = Entry(Point(230, 155), 5)
    E3.draw(win)
    E3.setText("")

    

    T5 = Text(Point(190, 180), "")
    T5.draw(win)
    T5.setText("Smash Success Rate")

    E5 = Entry(Point(170, 205), 5)
    E5.draw(win)
    E5.setText("")
    T6 = Text(Point(200, 205), "")
    T6.draw(win)
    T6.setText("/")
    E6 = Entry(Point(230, 205), 5)
    E6.draw(win)
    E6.setText("")

    T7 = Text(Point(198, 230), "")
    T7.draw(win)
    T7.setText("Drop Shot Success Rate")

    E7 = Entry(Point(170, 255), 5)
    E7.draw(win)
    E7.setText("")
    T8 = Text(Point(200, 255), "")
    T8.draw(win)
    T8.setText("/")
    E8 = Entry(Point(230, 255), 5)
    E8.draw(win)
    E8.setText("")

    T9 = Text(Point(50, 280), "")
    T9.draw(win)
    T9.setText("Analysis")
    T10 = Text(Point(150, 320), "")
    T10.draw(win)

    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            name = E1.getText()

            text1 = E2.getText()
            num1 = int(text1)
            text2 = E3.getText()
            num2 = int(text2)
            text3 = E5.getText()
            num3 = int(text3)
            text4 = E6.getText()
            num4 = int(text4)
            text5 = E7.getText()
            num5 = int(text5)
            text6 = E8.getText()
            num6 = int(text6)
            
            HS = num1/num2
            S = num3/num4
            LS = num5/num6
            T10.setText("The Success Rate of High Serve: " + str(round(HS, 2)) + "\nThe Success Rate of Smash: " + str(round(S,2)) + "\nThe Success Rate of Drop Shot: " + str(round(LS,2)) )
        if B2.isClicked(m):


        


            win2 = GraphWin("Graph vs. " + name, 550, 550)
            

            
            #X-Axis, Y-Axis, and Lables
            X = Line(Point(0, 50), Point(550, 50))
            X.draw(win2)
            X1 = Text(Point(540, 40), "")
            X1.draw(win2)
            X1.setText("x")
            X2 = Text(Point(275, 40), "")
            X2.draw(win2)
            X2.setText("Scored")
            Y = Line(Point(50, 0), Point(50, 550))
            Y.draw(win2)
            Y1 = Text(Point(40, 540), "")
            Y1.draw(win2)
            Y1.setText("y")
            Y2 = Text(Point(25, 275), "")
            Y2.draw(win2)
            Y2.setText("Attempts")
            XY = Text(Point(40, 40), "")
            XY.draw(win2)
            XY.setText("0")

            #Grids - X
            G = Text(Point(100, 50), "")
            G.draw(win2)
            G.setText("2\n|")
            
            G = Text(Point(150, 50), "")
            G.draw(win2)
            G.setText("4\n|")
            
            G = Text(Point(200, 50), "")
            G.draw(win2)
            G.setText("6\n|")
            
            G = Text(Point(250, 50), "")
            G.draw(win2)
            G.setText("8\n|")
            
            G = Text(Point(300, 50), "")
            G.draw(win2)
            G.setText("10\n|")

            G = Text(Point(350, 50), "")
            G.draw(win2)
            G.setText("12\n|")
            
            G = Text(Point(400, 50), "")
            G.draw(win2)
            G.setText("14\n|")
            
            G = Text(Point(450, 50), "")
            G.draw(win2)
            G.setText("16\n|")

            G = Text(Point(500, 50), "")
            G.draw(win2)
            G.setText("18\n|")

            #Grids - Y
            G = Text(Point(50, 100), "")
            G.draw(win2)
            G.setText("2----")
            
            G = Text(Point(50, 150), "")
            G.draw(win2)
            G.setText("4----")
            
            G = Text(Point(50, 200), "")
            G.draw(win2)
            G.setText("6----")
            
            G = Text(Point(50, 250), "")
            G.draw(win2)
            G.setText("8----")
            
            G = Text(Point(50, 300), "")
            G.draw(win2)
            G.setText("10----")

            G = Text(Point(50, 350), "")
            G.draw(win2)
            G.setText("12----")
            
            G = Text(Point(50, 400), "")
            G.draw(win2)
            G.setText("14----")
            
            G = Text(Point(50, 450), "")
            G.draw(win2)
            G.setText("16----")

            G = Text(Point(50, 500), "")
            G.draw(win2)
            G.setText("18----")

            

            #Points
            point1 = Text(Point(num1*25+50, num2*25+50), "")
            point1.draw(win2)
            point1.setText("X")
            p1 = Text(Point(210, 530), "")
            p1.draw(win2)
            p1.setText("X: High Serve")

            point2 = Text(Point(num3*25+50, num4*25+50), "")
            point2.draw(win2)
            point2.setText("Y")
            p2 = Text(Point(275, 530), "")
            p2.draw(win2)
            p2.setText("Y: Smash")

            point3 = Text(Point(num5*25+50, num6*25+50), "")
            point3.draw(win2)
            point3.setText("Z")
            p3 = Text(Point(340, 530), "")
            p3.draw(win2)
            p3.setText("Z: Drop Shot")

            
        if Q.isClicked(m):

            break

    win.close()
    win2.close()



if __name__=="__main__":
    main()
