input_str = str(input("Enter the String :"))

for char in input_str :
    print(char)
    if input_str.count(char) == 1 :
        print("First non-repeated char is : ", char)
        break