import random

def main():

    sample1 = open("FourSyllable.txt")
    myString1 = sample1.read()
    myList1 = myString1.split()
    

    sample2 = open("ThreeSyllable.txt")
    myString2 = sample2.read()
    myList2 = myString2.split()
    

    sample3 = open("TwoSyllable.txt")
    myString3 = sample3.read()
    myList3 = myString3.split()
    

    sample4 = open("OneSyllable.txt")
    myString4 = sample4.read()
    myList4 = myString4.split()


    # Generate first sentence (5 syllables) 4-1
    firstline = ("{0} {1}")
    print(firstline.format(random.choice(myList1), random.choice(myList4)))


    # Generate second sentence (7 syllables) 1-2-3-1
    secondline = ("{0} {1} {2} {3}")
    print(secondline.format(random.choice(myList4), random.choice(myList3), random.choice(myList2), random.choice(myList4)))


    # Generate third sentence (5 syllables) 1-3-1
    thirdline = ("{0} {1} {2}")
    print(thirdline.format(random.choice(myList4), random.choice(myList2), random.choice(myList4)))

    



if __name__=="__main__":
    main()
