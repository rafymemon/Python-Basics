age = input("Age of the User :")

age_in_int = int(age)

if age_in_int < 13:
    print("User is a Child")
elif age_in_int < 20:
    print("User is a Teenager")
elif age_in_int < 60:
    print("User is an Adult")
else:
    print("User is a Senior")
