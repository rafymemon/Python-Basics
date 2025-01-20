age = input("Age of the customer : ")
age_in_int = int(age)
day = input("Mention the day of the ticket booking :")

price = 12 if age_in_int >= 18 else 8

if day == "Wednesday":
    price -= 2
    # price = price - 2

print("Ticket Price for you is $", price)
