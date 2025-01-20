
fruit = input("Enter the fruit name :")

if fruit == "banana" :
    color = input("Enter color :")
    if color == "Green" :
        print("Your fruit is unripe")
    elif color == "Yellow" :
        print("Your fruit is perfectly ripe.")
    elif color == "Brown" :
        print("Your fruit is overripe.")
    else :
        print("Enter the correct fruit...")
else:
  print("Your fruit is not banana")     
  exit() 