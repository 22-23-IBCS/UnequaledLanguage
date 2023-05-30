from graphics import*
from Button import*
import math
def main():
    win = GraphWin("Badminton Stats Analysis", 520, 380)
    win.setBackground("grey18")
    T = Text(Point(50, 10), "")
    T.draw(win)
    T.setText("Information")
    T.setFill("LavenderBlush4")

    Q = QuitButton(win, Point(300, 250), Point(380, 270))
    B1 = Button(win, Point(300, 180), Point(380, 200), "dodger blue", "Confirm Data")
    B2 = Button(win, Point(300, 215), Point(380, 235), "dodger blue", "Create Graph")
    

    T1 = Text(Point(100, 40), "")
    T1.draw(win)
    T1.setText("Opponent Name:")
    T1.setFill("LavenderBlush4")
    


    E1 = Entry(Point(200.5, 40), 10)
    E1.draw(win)
    E1.setFill("grey18")
    E1.setTextColor("White")

    T2 = Text(Point(50, 100), "")
    T2.draw(win)
    T2.setText("Stats")
    T2.setFill("LavenderBlush4")

    T3 = Text(Point(200, 130), "")
    T3.draw(win)
    T3.setText("High Serve Success Rate")
    T3.setFill("LavenderBlush4")

    E2 = Entry(Point(170, 155), 5)
    E2.draw(win)
    E2.setText("")
    E2.setFill("grey18")
    E2.setTextColor("White")
    T4 = Text(Point(200, 155), "")
    T4.draw(win)
    T4.setText("/")
    E3 = Entry(Point(230, 155), 5)
    E3.draw(win)
    E3.setText("")
    E3.setFill("grey18")
    E3.setTextColor("White")

    

    T5 = Text(Point(190, 180), "")
    T5.draw(win)
    T5.setText("Smash Success Rate")
    T5.setFill("LavenderBlush4")

    E5 = Entry(Point(170, 205), 5)
    E5.draw(win)
    E5.setText("")
    E5.setFill("grey18")
    E5.setTextColor("White")
    T6 = Text(Point(200, 205), "")
    T6.draw(win)
    T6.setText("/")
    T6.setFill("LavenderBlush4")
    E6 = Entry(Point(230, 205), 5)
    E6.draw(win)
    E6.setText("")
    E6.setFill("grey18")
    E6.setTextColor("White")

    T7 = Text(Point(198, 230), "")
    T7.draw(win)
    T7.setText("Drop Shot Success Rate")
    T7.setFill("LavenderBlush4")

    E7 = Entry(Point(170, 255), 5)
    E7.draw(win)
    E7.setText("")
    E7.setFill("grey18")
    E7.setTextColor("White")
    T8 = Text(Point(200, 255), "")
    T8.draw(win)
    T8.setText("/")
    T8.setFill("LavenderBlush4")
    E8 = Entry(Point(230, 255), 5)
    E8.draw(win)
    E8.setText("")
    E8.setFill("grey18")
    E8.setTextColor("White")

    T9 = Text(Point(50, 280), "")
    T9.draw(win)
    T9.setText("Analysis")
    T9.setFill("LavenderBlush4")
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
            T10.setFill("gainsboro")
        if B2.isClicked(m):


        


            win2 = GraphWin("Graph vs. " + name, 550, 550)
            win2.setBackground("grey14")
            

            
            #X-Axis, Y-Axis, and Lables
            X = Line(Point(0, 50), Point(550, 50))
            X.draw(win2)
            X.setFill("grey81")
            X1 = Text(Point(540, 40), "")
            X1.draw(win2)
            X1.setText("x")
            X1.setFill("grey81")
            X2 = Text(Point(275, 30), "")
            X2.draw(win2)
            X2.setText("Scored")
            X2.setFill("grey81")
            Y = Line(Point(50, 0), Point(50, 550))
            Y.draw(win2)
            Y.setFill("grey81")
            Y1 = Text(Point(40, 540), "")
            Y1.draw(win2)
            Y1.setText("y")
            Y1.setFill("grey81")
            Y2 = Text(Point(25, 275), "")
            Y2.draw(win2)
            Y2.setText("Attempts")
            Y2.setFill("grey81")
            XY = Text(Point(40, 40), "")
            XY.draw(win2)
            XY.setText("0")
            XY.setFill("grey81")
            xy = Line(Point(50,50), Point(550, 550))
            xy.draw(win2)
            xy.setFill("grey81")
            xy1 = Text(Point(520, 480), "")
            xy1.draw(win2)
            xy1.setText("100% Line")
            xy1.setFill("grey81")

            #Grids - X
            G = Text(Point(100, 50), "")
            G.draw(win2)
            G.setText("2\n|")
            G.setFill("grey81")
            
            G = Text(Point(150, 50), "")
            G.draw(win2)
            G.setText("4\n|")
            G.setFill("grey81")
            
            G = Text(Point(200, 50), "")
            G.draw(win2)
            G.setText("6\n|")
            G.setFill("grey81")
            
            G = Text(Point(250, 50), "")
            G.draw(win2)
            G.setText("8\n|")
            G.setFill("grey81")
            
            G = Text(Point(300, 50), "")
            G.draw(win2)
            G.setText("10\n|")
            G.setFill("grey81")

            G = Text(Point(350, 50), "")
            G.draw(win2)
            G.setText("12\n|")
            G.setFill("grey81")
            
            G = Text(Point(400, 50), "")
            G.draw(win2)
            G.setText("14\n|")
            G.setFill("grey81")
            
            G = Text(Point(450, 50), "")
            G.draw(win2)
            G.setText("16\n|")
            G.setFill("grey81")

            G = Text(Point(500, 50), "")
            G.draw(win2)
            G.setText("18\n|")
            G.setFill("grey81")

            #Grids - Y
            G = Text(Point(50, 100), "")
            G.draw(win2)
            G.setText("2----")
            G.setFill("grey81")
            
            G = Text(Point(50, 150), "")
            G.draw(win2)
            G.setText("4----")
            G.setFill("grey81")
            
            G = Text(Point(50, 200), "")
            G.draw(win2)
            G.setText("6----")
            G.setFill("grey81")
            
            G = Text(Point(50, 250), "")
            G.draw(win2)
            G.setText("8----")
            G.setFill("grey81")
            
            G = Text(Point(50, 300), "")
            G.draw(win2)
            G.setText("10----")
            G.setFill("grey81")

            G = Text(Point(50, 350), "")
            G.draw(win2)
            G.setText("12----")
            G.setFill("grey81")
            
            G = Text(Point(50, 400), "")
            G.draw(win2)
            G.setText("14----")
            G.setFill("grey81")
            
            G = Text(Point(50, 450), "")
            G.draw(win2)
            G.setText("16----")
            G.setFill("grey81")


            G = Text(Point(50, 500), "")
            G.draw(win2)
            G.setText("18----")
            G.setFill("grey81")
            

            #Points
            point1 = Text(Point(num1*25+50, num2*25+50), "")
            point1.draw(win2)
            point1.setText("X")
            point1.setFill("grey81")
            p1 = Text(Point(210, 530), "")
            p1.draw(win2)
            p1.setText("X: High Serve")
            p1.setFill("grey81")

            point2 = Text(Point(num3*25+50, num4*25+50), "")
            point2.draw(win2)
            point2.setText("Y")
            point2.setFill("grey81")
            p2 = Text(Point(275, 530), "")
            p2.draw(win2)
            p2.setText("Y: Smash")
            p2.setFill("grey81")

            point3 = Text(Point(num5*25+50, num6*25+50), "")
            point3.draw(win2)
            point3.setText("Z")
            point3.setFill("grey81")
            p3 = Text(Point(340, 530), "")
            p3.draw(win2)
            p3.setText("Z: Drop Shot")
            p3.setFill("grey81")

            
        if Q.isClicked(m):

            break

    win.close()
    win2.close()



if __name__=="__main__":
    main()
