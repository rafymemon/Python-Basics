# String
print("String Data Type\n")
username = "Rafy Mustafa"
print(len(username))

print(username[3])
print(username[-1])  # output --> a
print(username[2:6])  # output --> fy M

print(
    dir(username)
)  # dir functions shows the number of functions that can be used with strings
print("\n")

# List
print("List Data Type\n")
myList = [123, "Software Engineer", 3.14]
print(myList)

print(len(myList))
print(myList[2])
print(myList[-2])

print("\n")

# Dictionaries
print("Dictionary Data Type\n")
myD = {"Name": "Rafy Mustafa", "Department": "Software Engineering", "Hobbies": "Books"}
print(myD)

print(myD["Name"])
print(myD["Hobbies"])
print(len(myD))

print("\n")

# Tuple

print("Tuple Data Type\n")
myTup = (1, "Rafy", 2, 34)

print(myTup)
print(myTup[1])
print(myTup[3])
print(len(myTup))
