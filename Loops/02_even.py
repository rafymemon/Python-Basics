n = int(input("Enter the numbers"))
even_numbers = 0

for i in range(1, n+1) :
    if i% 2 == 0 :
        even_numbers +=i
        
print("Sum of the even numbers are : ", even_numbers)