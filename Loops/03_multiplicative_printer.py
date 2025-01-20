number = int(input(" Enter the number :"))

for i in range(1, 11) :
    if i == 5 :
        continue # continue keyword is used to skip the perticular iteration 
    print(number, 'x', i, '=', number * i)
    
    
