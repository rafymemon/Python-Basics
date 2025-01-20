
password = input("Enter the password :")


if len(password) < 6 :
    seurity = "Weak"
elif len(password) in range(6, 10) :
    security = "Medium"
else :
    security = "Strong"
    
print("Your password is :", security)