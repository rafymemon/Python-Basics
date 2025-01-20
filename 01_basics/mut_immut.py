# immutable Objects : Immutable objects can't be changed after creation. Any operation that modifies an immutable objects creates a new object instead

username = "Rafy"
print(username)  #here, username containing the value "Rafy"

username = "Channge User name"
print(username) # when we change the value from "Rafy" to "change user name", it will create a new object of username while the initial object will be deleted from the memory 
                #by garbage collector..


x = 10
y = x
print(x)
print(y)

x = 15
print(x)
print(y)
