def dollarstreet():
    brand = ["Ford", "Toyota", "Honda", "Suzuki", "Mini", "Citroen"]
    income = [1000, 2000, 500, 2500, 3500, 4000]
    mean = 0
    for i in income:
        mean = mean + i

    average = mean / len(income)
    u = input("Enter a brand ")


    for i in range(len(brand)):

        if u==brand[i]:
            userIncome=income[i]
            if userIncome==average:
                print("you are average")
            elif userIncome<average:
                print("you are below average")
            elif userIncome>average:
                print("you are above average")


def main():
    dollarstreet()


if __name__=="__main__":
    main()



