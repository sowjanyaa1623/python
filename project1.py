#Project:Get the student name and marks, find the average and use conditional to give grades.
#print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

student_name=input("enter your name: " )
student_mark1=int(input("enter your tamil: "))
student_mark2=int(input("enter your english: "))
student_mark3=int(input("enter your maths: "))
student_mark4=int(input("enter your science: "))
student_mar5k=int(input("enter your social: "))
total=student_mark1+student_mark2+student_mark3+student_mark4+student_mark5
average=total/5
print("the average mark of the student: average")
if average<=100 and average<=90:
    print("your grade is A")
elif average <=89 and average <= 80:
    print("your grade B")
elif average<=79 and average<=70:
    print("your grade is C")
elif average <= 69 and average <= 60:
    print("your grade is D")
else:
    print("your grade is E")


