
marks = input("Enter your marks")
marks_int = int(marks)

if marks_int >= 101 :
    print("Please verify your grade..")
    exit()
if marks_int >= 90 :
    grade = "A"
elif marks_int >= 80  :
    grade = "B"
elif marks_int  >= 70:
    grade = "C"
elif marks_int  >= 60 :
    grade = "D"
else :
    grade = "F"
    
print("Your grade is :",grade)
    