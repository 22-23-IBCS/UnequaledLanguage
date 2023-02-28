import random

def genLine(syl, val, letter):
    line = ""
    while True:
        v = random.randint(1,4)
        if val - v >= 0:
            myList = syl.get(v).split()

            myListA = [word for word in myList if letter not in word]


            line = line + random.choice(myListA) + " "
            val = val - v
        if val == 0:
            break
    
    return line

def main():
    f1 = open("oneSyllable.txt")
    f2 = open("twoSyllable.txt")
    f3 = open("threeSyllable.txt")
    f4 = open("fourSyllable.txt")
    readOne = f1.read()
    readTwo = f2.read()
    readThree = f3.read()
    readFour = f4.read()
    syl = {1 : readOne,
           2 : readTwo,
           3 : readThree,
           4 : readFour}
    letter = input("Enter a letter to eliminate from the haiku: ")
    print(genLine(syl, 5, letter))
    print(genLine(syl, 7, letter))
    print(genLine(syl, 5, letter))

if __name__ == "__main__":
    main()
