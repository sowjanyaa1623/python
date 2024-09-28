
#no.1

# Get input from the user as age
# If age is lesser than 0,it considers it invalid
# If the age is between 0 and 17 (inclusive), it considers the user a minor.
# If the age is between 18 and 64 (inclusive), it considers the user an adult.
# If the age is 65 or older, it considers the user a senior citizen.

age=int(input("enter your age: "))
if age<0:
    print("invalid")
elif age<=17:
    print("minor")
elif age>=18 and age<65:
    print("adult")
else:
    print("senior citizen")

#no.2

# Get the age from user,
# if age is less than 18, print "you are not eligible"
# if age is greater than 18 and less than 60,
# Print"you are eligible to attend the event"
# if age is above 60, print"you are too old ,
# so not able to attend the event"

# age=int(input("enter your age: "))
# if age<18:
#     print("you are not eligible")
# elif age>=18 and age<60:
#     print("you are eligible to attend the event")
# else:
#     print("you are too old so not able to attend the event")

#no.3

# Get input for the total purchase amount and membership status (yes or no).
# If the purchase amount is greater than or equal to $100 and the user is a member:
# Calculate and print the discounted price as 10% off the total purchase amount.
# If the purchase amount is less than $100 or the user is not a member:
# Print the message "No discount available."

# amount=int(input("enter the total purchase amount: "))
# status=input("do you have a membership: ")
# if amount>=100 and status=="yes":
#     amount = amount * 10 / 100
#     print("discounted price:", amount,end="$,")
#     print("you got discount of 10%")
# elif amount<100 or status=="no":
#     print("No discount available.")