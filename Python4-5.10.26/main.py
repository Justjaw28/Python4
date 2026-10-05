print ("Select a random number")
choice = int(input("Enter your choice: "))
if choice > 0 :
    print("You selected a positive number.")
else:
    if choice < 0:
        print("You selected a negative number.")
        print("The absolute value of your choice is:", -choice)
    else:
        print("You selected zero.")