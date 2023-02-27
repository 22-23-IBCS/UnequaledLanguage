import random
import math
#1
def centralten(x, y, z):
    #mean
    mean = (x + y + z)/3

    #median
    if x < y:
        if y < z:
            median = y
        else:
            if x < z:
                median = z
            else:
                median = x
    else:
        if x < z:
            median = x
        else:
            if y < z:
                median = z
            else:
                median = y
    return 'mean', mean, 'median', median
#2
def rand0m():
    a = random.randint(1,100)
    if (a%2==0 or a%3==0 or a%5==0):
        return a, True
    else:
        return a, False
#3
def lists():
    L=[random.randint(1, 50) for i in range(10)]
    Max=max(L)
    Min=min(L)
    Range=(int(Max) - int(Min))
    return 'list', L, 'max', Max,'min', Min, 'range', Range
#4
def polarcoordinate(q,p):
    #distance
    p=[q,p]
    p0=[0, 0]
    Point = math.dist(p, p0)
    #angle
    h = Point
    
    #angle = math.degrees(math.asin(p[1]/h))
    angle = (math.asin(p[1]/h))*360/(2*math.pi)
    '''tan= (p[1]/p[0])
    a = math.atan(tan)
    angle = abs(math.degrees(a))'''
    return [h, angle]
#5
def scrpts():
    score = 0
    name = input("Type a name: ")
    name = name.lower()
    for char in name:
        if char in ["a", "i", "e", "o", "u", "l", "n", "r", "s", "t"]:
            score = score + 1
        elif char in ["d", "g"]:
            score = score + 2
        elif char in ["b", "c", "m", "p"]:
            score = score + 3
        elif char in ["f", "h", "v", "w", "y"]:
            score = score + 4
        elif char in ["k"]:
            score = score + 5
        elif char in ["j", "x"]:
            score = score + 8
        else:
            score = score + 10
    return score
o
def main():
        print(centralten(3, 5, 6))
        print(rand0m())
        print(lists())
        print(polarcoordinate(2,2))
        print(scrpts())
        


if __name__=="__main__":
    main()
