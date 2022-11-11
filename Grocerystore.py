class GroceryStore:
    def main():
        #Menu
        products=["","milk", "ice cream", "apple", "banana", "cherry", "meat", "fish", "juice", "bread", "rice"]
        price   =["","3.89", "4.99", "1.5", "2.99", "2.89", "4.89", "4.99", "3.5", "2.5", "1.5"]
        print("-Products-\n1.Milk-3.89$\n2.Ice cream-4.99$\n3.Apple=1.5$\n4.Banana-2.99$\n5.Cherry-2.89$\n6.Meat-4.89$\n7.Fish-4.99$\n8.Juice-3.5$\n9.Bread-2.5$\n10.Rice-1.5$")
        #Asking first products
        ask=int(input("Which products do you want to buy? "))

        print("You choose " + products[ask] + ", " + "the price is " + price[ask] + "$")
        total = price[ask]
        print("Total price: " + str(total)+"$")
        ask1=input("Anything else? (Yes or No)")

        #Loops for asking more
        if (ask1 == "Yes"):
            while (ask != 0):
                ask=int(input("Which products do you want to buy? - Press 0 to check out "))
                if (ask !=0):

                    print("You choose " + products[ask] + ", " + "the price is " + price[ask] + "$")
                    totaln= price[ask]
                    total= float(total) + float(totaln)
                    print("Total price: " + str(total)+"$")

        #Total cost
        print("Your total cost: " + str(total) + "$")
    if __name__ == "__main__":
        main()
        
        
    
