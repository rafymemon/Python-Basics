information = {
    "First_Name": "Rafy",
    "Last_Name": "Mustafa",
    "Semester": "Fifth semester",
    "CGPA": "3.01",
}

#print(information)
#print(information["First_Name"])  # Accessing any perticular value using the key
# Methods in dictionary
#print(information.get("Last_Name"))

information["CGPA"] = "2.56"
#print(information)


# for info in information:
# print(info, information[info])

# For loop is used to access keys and values(This pattern is only for dictionaries)
# for key, value in information.items() :
#  print(key, value)


# using if conditions to check wether a key is present in the dictionary
if "First_Name" in information:
    print("yes, First name is present")
else:
    print("No, First name is not mentioned in the dictionary")


print(
#    len(information)
)  # key and value is combinely called one item, len() is used to calculate the total length of the items
# Adding items in the dictionary
information["Department"] = "Software Engineering"
#print(information)

# Deleting an item
# print(information.pop("CGPA"))
# Deleting the last item
# print(information.popitem())
# print(information)

# another method of deleting any item
# del information["Semester"]
# print(information)

# Copy of the existing dictionry
info_copy = information.copy()
#print(info_copy)

# Multiple dictionaries in a large dictionary(Metrics)
Departments_information = {
    "Software Department": {
        "Chairman": "Dr Qasim Ali",
        "Vice Chairman": "prof. Mohsin Memon",
        "Students": "400"
    },
    "Electrical": {
        "Chairman": "Asif Ali Shah",
        "Vice Chairman": "Ali Asghar",
        "Students": "300",
    },
    "Electronics": {
        "Chairman": "Nadeem Ahmed",
        "Vice Chairman": "prof. siddique",
        "Students": "350",
    },
}
#print(Departments_information["Software Department"]["Chairman"])

# Squared numbers
squared_nums = {x:x**2 for x in range(6)}
#print(squared_nums)


keys = ["Name","Department", "Semester", "CGPA"]
default_value = "xyz"
new_dictionary = dict.fromkeys(keys, default_value)
print(new_dictionary)