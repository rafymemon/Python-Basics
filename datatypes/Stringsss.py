
game = "Cricket"
first_char = game[0]
slice_char = game[0:4]
slice_secChar = game[::2]
#print("game")
#print(first_char) # output : p
# print(game[1:4]) #output : ric (slicing)
# print(game[::2]) # output : cikt (slicing every 2nd character)

#print(slice_char)
#print(slice_secChar)

numbers = "0123456789"

#print("Slicings types....")
slice_one = numbers[0:9] # numbers[:] both output will be same
slice_two = numbers[:7]
slice_three = numbers[3:]
slice_four = numbers[0:7:2] # Slicing from 0 to 6 with hopping of every second character

# print(slice_one)
# print(slice_two)
# print(slice_three)
# print(slice_four)


print("Methods in Strings....")

name = "   Rafy Mustafa  "
# lower
print(name.lower())
#upper
print(name.upper())
# Strip : 
# use to cancel out extra space
print(name.strip())
# replace : used to replace any perticular characters
print(name.strip().replace("Rafy", "Shafy"))
# Split: Use to convert string into list based on delimiter
print(name.strip().split(" "))
print("I am learning machine learning".split())
#Find
print(name.strip().find("Mustafa"))
#Count
print(name.count("a"))

#order formating

String_type = "python"
time = 2
order = "I give {} hours to {} daily" # order formating

print(order.format(time, String_type))

# list to string
my_list = ["Rafy", "Memon", "3GPA"]

print(", ".join(my_list))

# Legth of the string
print(len(name))