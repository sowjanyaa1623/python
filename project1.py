#Project:Get the student name and marks, find the average and use conditional to give grades.
#print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

student_name=input("enter your name: " )
student_standard=int(input("enter your standard: "))
number_of_subjects=5
student_mark1=int(input("enter your tamil marks : "))
student_mark2=int(input("enter your english marks : "))
student_mark3=int(input("enter your maths marks : "))
student_mark4=int(input("enter your science marks : "))
student_mark5=int(input("enter your social marks : "))
total_marks= student_mark1+student_mark2+student_mark3+student_mark4+student_mark5
average_marks =total_marks/number_of_subjects
print("the average mark of the student:", average_marks)
print("the total mark of the student:", total_marks)
if average_marks<=100 and average_marks>=90:
    print("your grade is A")
elif average_marks <=89 and average_marks >=80:
    print("your grade B")
elif average_marks<=79 and average_marks>=70:
    print("your grade is C")
elif average_marks<= 69 and average_marks >=60:
    print("your grade is D")
else:
    print("your grade is E")


