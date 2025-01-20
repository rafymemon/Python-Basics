import random

random.random()

print(random.randint(1, 100))
print(random.randint(1, 100))


l1 = [12, 23, 43, 54, 53]

print(random.choice(l1))
print("\n")
print("L1 before shuffle :", l1)


random.shuffle(l1)
print("L1 after shuffle:", l1)


# Adding a random number in the list
my_list = [12, 43, 54, 23, 34, 55, 93]
print("List before updation:", my_list)

random_number = random.randint(1, 100) # generate a random number between 1 to 100

random_index = random.randint(0, len(my_list)) # to get random index to add the number

my_list.insert(random_number, random_index) # insert the random number in the random index

print("updated list:", my_list, "\n") # List after updation

print(random.choice(my_list))
print(random.uniform(23, 43))

# print (n) numbers from the list 
sample_number = random.sample(my_list, 3)
print(sample_number)
