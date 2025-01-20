order = input("Enter your order")
Extra_shot = input("Do you want an extra shot")



if order == "Medium" :
    coffee = "Medium Coffee"
elif order == "Small" :
    coffee = "Small Coffee"
elif order == "Large" :
    coffee = "Large Coffee"
else :
   print(order, "incorrect")
   exit()
    
if Extra_shot == "True" :
    print(coffee, "With Extra Shot")
elif Extra_shot == "False" :
    print(coffee)
else :
    print("Mention wether to add Extra shot or not?")


