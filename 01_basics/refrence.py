import sys

# print(sys.getrefcount(24601))

# print(sys.getrefcount(('Rafy')))

# a = 3
# a = "Rafy"
# a = 3.14


a = 5
b = 2
a = a + 2
print(a)

myListOne = [1, 2, 3, 4]
myListTwo = myListOne
# myListOne = "Student"

print(myListOne)
print(myListTwo)

myListOne[0] = 33
print(myListOne)  # output = [33, 2, 3, 4]
print(myListTwo)  # output = [33, 2, 3, 4] output is same because myListOne and myListTwo is having same refrence
print("\n")


list1 = [1, 2, 3]
list2 = list1

list2 = [1, 2, 3]
list1[0] = 33

print(list1)
print(list2)
print("\n")
# Here the output will be changed because at first we have gien the same refrence but then list2 is given a separate value in the memory therefore the change will only be applicable to list1


h1 = [1, 2, 3]
h2 = h1[:] # It means h2 is a copy of h1, changing in h1 will affect h2

h1[0] = 22
print(h1)
print(h2) 
print("\n")

n = [1, 2, 3, 4]
m = n

print(m)
print(m == n) # checks that either the value of both objects are same, if yes it prints True

print(m is n) # "is" checks that either the memory objects refrence are same, if yes then print True

n = [12, 2, 3, 4]
print(m is n)