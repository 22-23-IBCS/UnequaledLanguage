# IBCS "Find my error"
import random
# Each method below currently does not run properly. Either it throws an error
# or it prints out/returns the wrong thing. Fix each method one by one.
# Comment out the method call in the main to run it and test it.


#calculate sum, product and mean of three numbers
def calcThree(a, b, c):
    x = a + b + c
    y = a*b*c
    z = (a+b+c)/3
    return x, y, z

#determine the minimum value in a list of numbers
def myMin(L):
    m = min(L)

    return m

#determine the average number of characters in a word
def sentenceData():
    sen = input("Please type a sentence.\n")
    senWords = sen.split()
    numWords = len(senWords) #total words
    totalChar = 0
    for w in range(len(sen)):
        totalChar = w
    print("The average word length is: " + str(round(totalChar/numWords, 2)) )

#randomize the characters in a user input name (First and Last)
# and print out the users new name
def randomName():
    name = input("Please enter your first name ")
    name2 = input("Please enter your last name ")
    newname1=""
    newname2=""

    for n in name:
        newname1 = newname1 + random.choice(name)
    for n in name2:
        newname2 = newname2 + random.choice(name2)

    print("Hello " + newname1 + " " + newname2)


def main():
    #print(calcThree(1,2,3))
    #print(myMin(L=[1,2,3,4,5,6,7,0,8,9,10]))
    #sentenceData()
    randomName()

if __name__ == "__main__":
    main()
