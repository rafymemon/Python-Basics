

dept_name = ["Software", "Electrical", "Civil", "Mechanical"]

print(dept_name)

print(dept_name[0:])
print(dept_name[:4])
print(dept_name[0::4])

dept_name[3] = "Chemical"
print(dept_name)

#for dept in dept_name:
 #   print(dept, end="-",)
    
#if "PG" in dept_name:
 #   print("yes")
#else:
 #   dept_name.append("PG")
  #print(dept_name)
  
  
print(dept_name.pop()) # pop() is used to delete the last value of the list

dept_name.remove("Software") # remove() is used to delete any intended item from the list
print(dept_name)

dept_name.insert(0, "Software") # insert() is used to add any item at the intended position in the list
print(dept_name)

dept_name_two = dept_name.copy() # copy() method is used to copy the existing element in a list two the new list and the new list have a seprate refrence in the memory
print(dept_name_two)

dept_name_two.append("Textile")
print(dept_name_two)

# list Comprehension
squared_num = [x**2 for x in range(10)]
print(squared_num) # 0 1 4 9 16 25 36 49 64 81