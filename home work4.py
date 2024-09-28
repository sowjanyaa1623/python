#home work
#get a string from user check wherther it's a palindrome or not

string=input("enter your string: ")
palindrome=string[::-1]
if string==palindrome:
    print("your string is a palindrome")
else:
    print("your string is not a palindrome")


#get two string from user check wherther it's a anagram or not
#from pickletools import string

string1=input("enter your 1st string: ")
string2=input("enter your 2nd string: ")
if sorted(string1)==sorted(string2):
    print("your string is an anagram")
else:
    print("your string is not an anagram")