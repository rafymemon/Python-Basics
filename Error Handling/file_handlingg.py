file = open("f:/python_programs/Error Handling/abcdef.txt", "r")
text = file.read()
print(text)
file.close()

with open("f:/python_programs/Error Handling/abcdef.txt", 'a') as f :
    f.write("\nPython is a language that is easy to use")

# Types for file handling
# Both the files are used for file handling

#try :
 #   file.write("Example of file handling")
    
#finally :
 #   file.close()
    
    
    
#with open('abc.txt', 'w') as file :
 #   file.write("Example of file handling")