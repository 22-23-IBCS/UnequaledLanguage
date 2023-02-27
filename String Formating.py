def greeting():
    name = input("Giver a name\n")
    return "Hello, " + name + ", Welcome to CS Class."





def main():
    # File handling
    '''sample = open("samepleText.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word=word.lower()
        if "un" in word:
            print(word)'''
            

    

    # String formating
    # Creat place-holders for various and "fields"
    # Print things with the place-holders substiting different values

    name = "Mr. Considine"
    greeting = "Hello, {}. welcome to CS Class."
    # Change place-holders with the value of names
    # By using .format --> pass in whatever value in the brace
    print(greeting.format(name))
    name = "Frank"
    print(greeting.format(name))

    text = "Congrats, {}. You got a {} on the final exam"
    name = "Mr. Phillips"
    grade = 99
    print(text.format(name, grade))
    #using {1} and {0} can indicate the value that u pass in regardless of the position in the .format command
    #Can also format intergers and floats
    price = 4.6799999
    txt = "Yikes, gas costs ${:2f} a gallon"
    # : represent round, 2 represent decimal place, f is floats
    print(txt.format(price))

if __name__=="__main__":
    main()
