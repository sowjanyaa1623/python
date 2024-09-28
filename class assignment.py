#prject1

#Find out the climate, if it is hot, print "cant playgames", if it is cool, "jolly, we can play games"

# climate=(input("enter the climatic condition: "))
# climate=climate.upper()
# if climate=="HOT" or climate=="NOT COLD":
#     print("we can't play game")
# else:
#     print("jolly, we can play games")

# Checking if a number is both  positive and even

# number=int(input("enter a number: "))
# if (number>0 and number%2 == 0) :
#     print("it is a positive, even number")
# else:
#     print("it is not a positive even number")

#project2

# fruit=input("enter from strawberry,mango,orange: ")
# fruit=fruit.lower()
# if fruit=="strawberry":
#     print("red in colour")
# elif fruit=="mango":
#     print("yellow in colour")
# elif fruit=="orange":
#     print("orange in colour")
# else:
#     print("pick from the option")

#project3

# Checking if a number is both  positive and even

# number=int(input("enter a number: "))
# if (number>0 and number%2 == 0) :
#     print("it is a positive, even number")
# else:
#     print("it is not a positive even number")

#project4

#conditional staements if,else positive or not

#no.1
# number=int(input("enter a number: "))
# if number>0:
#     print("it is positive")
# else:
#     print("it is not positive")

#no.2
# age=int(input("enter your age: "))
# if age>=18:
#     print('you are eligible to vote')
# else:
#     print("you are not eligible tp vote")

#no.3
# fruit=input("enter the name of the fruit: ")
# fruit=fruit.upper()
# if fruit=="BANANA":
#     print("it is yellow in colour")
# else:
#     print("it is not yellow in colour")

#nested if and else.

#no.1

# bag=input("enter from banana,apple,guava,brinjal,potato,pumkin: ")
# bag=bag.lower()
# if bag=="banana" or bag=="apple" or bag=="guava":
#     print("it is a fruit")
#     if bag=="banana":
#         print("yellow")
#     elif bag=="apple":
#         print("red")
#     else :
#         print("green")
# elif bag=="brinjal" or bag=="potato" or bag=="pumkin":
#     print("it is a vegetable")
#     if bag=="brinjal":
#         print("purple")
#     elif bag=="potato":
#         print("brown")
#     else:
#         print("orange")
# else:
#     print("choose from the options")

# Get age from the user.
# If age is greater than or equal to 18.get height from
# the user.If not print(“Sorry you need to be atleast 18
# years old to ride”).if height is greater than or equal
# to 1.4 print(“you are eligible to ride the roller
# coaster”) else print(“Sorry,you need to be atleast 1.4
# meters tall to ride”)

#no.2

# age=int(input("enter your age: "))
# height=float(input("enter your height: "))
# if age>=18 and height>=1.4:
#     print ("you are eligible to ride the roller coaster")
# elif age<18:
#     print("Sorry, you need to be atleast 18 years to ride")
# else:
#     print("sorry you need to be atleast 1.4 meters tall to ride")

#no.3

# Get input for salary and age.
# If salary greater than or equal to 20000 and age less
# than or equal to 25,get input for required loan
# amount. If not print you are not eligible for loan.If
# required loan amount is less than or equal to 50,000
# print You are eligible for loan. If it is greater than
# 50,000 print maximum loan amount is 50000.

# salary=int(input("enter your salary: "))
# age=int(input("enter your age: "))
# if salary>=20000 and age<=25:
#     print("you are eligible for loan")
#     loan_amount=int(input("enter the required loan amount: "))
#     if loan_amount<=50000 :
#         print("you are eligible for loan")
#     elif loan_amount>50000 :
#         print("maximum loan amount is 50000")
# else:
#     print("you are not eligible for loan")

# #strings
#
# #no1
# word="mathematics"
# print(word[5])
# print(word[-3])
#
# #no2
# name="sowjanyaa"
# print(name[6])
# print(name[-3])

# #1length
# a="good morning, everyone!"
# print(len(a))
#
# #2upper()
# print(a.upper())
#
# #3lower()
# print(a.lower())
#
# #4capitalize()
# l="life is amazing"
# print(l.capitalize())
#
# #5title()
# print(l.title())
#
# #6count()
# text="english is my favourite subject"
# print(text.count("i"))
#
# #7find-writes the lowest value of a sub-string
# print(a.find("o"))
#
# #8replace
# text="I like play football"
# text=text.replace("football","basket ball")
# print(text)

## #9strip
# s="   m no   "
# print(s)
# print(s.strip)
#
# #10concatenation
# s1="hi"
# s2="bye"
# print(s1+" "+s2+"14")
#
# #11replication
# s1="hi"
# s2="bye"
# print(s1*3)
# print(s2*len(s1))
#
# #12sorted
# a="apPle"
# a=a.lower()
# print(sorted(a))
#
# # partition-always breaks into three parts
# g="nine,ten# eleven ,twelve"
# print(g.partition("#"))
# print(g.partition(","))
#
# #split
# line="home work and class work"
# print(line.split())
# print(line.split(";"))
#
# join
# sentence="home #work an#d clas#s work"()
# got=sentence.split(#)
#     print(got)
# print("jkl".join(got))







#loop

# for i in range(-5,5):
#     print(i)
#
# for i in range (0,10,5):
#     print(i)
#
# for i in range (1,12):
#     print(i)
#
# for i in range(5):
#     mark1=int(input("mark1: "))
#     mark2= int(input("mark2: "))
#     mark3= int(input("mark3: "))
#     mark4= int(input("mark4: "))
#     mark5= int(input("mark5: "))
#     total=mark1+mark2+mark3+mark4+mark5
#     print("sum",total)
#     print("-"*10)

# add = 0
# for i in range(25):
#      add += i
#      print(add)






