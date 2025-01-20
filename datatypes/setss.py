
set_one = {1, 2, 3, 4, 5, 6}
set_two = {3, 5, 6, 7, 8, 9, 10}

# Intersection of two sets 
#print(set_one & set_two) 
#print(set_one.intersection(set_two))

# Union of two sets
#print(set_one | set_two)
#print(set_one.union(set_two)) 
#print(set_one.update(set_two))

#Difference
#print(set_one - {1, 2, 3, 4, 5, 6}) # output will be (set()) because empty paranthesis are used for dictionaries
#print(set_one.difference(set_two))

#Symmetric difference
#print(set_one.symmetric_difference(set_two))

#There are several inbuilt methods used for the manipulation of the sets

# 1. isdisjoint() --> Boolean method that checks wether the items of the given set are present in the other set and return true or false accordinf to it
disjoint_set = set_one.isdisjoint(set_two)
print(disjoint_set)

# 2. issuperset()  --> checks if all the items of a perticular set are present in the original set. It returns true if all are persent else return false.
issuper_set = set_one.issuperset(set_two)
print(issuper_set)

# 3. issubset() --> Checks if all the items of the original set are present in the perticular set. Returns true if all the elements are present else return false.
issub_set = set_one.issubset(set_two)
print(issub_set)

# 4. add() --> used to add a single item in the set
sett = {"karachi", "Tokyo", "Delhi", "Berlin"}
sett.add("Geneva")
print(sett)

# print(type(True))

s = {1, 2, 3, 5, 6, 5}
print(s)

info = {"Rafy", 21, 2.6, 43, "Memon", 21}
print(info)

# Find the type of set
rafy = set()
print(rafy)



