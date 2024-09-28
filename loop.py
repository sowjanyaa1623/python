#loops

#for loop
# name="sowjanyaa"
# for i in name:
#     print(i)

#range(start,stop,step)
#range(1,11) 1,2,3,4,5,6,7,8,9,10

# #e.g.1
# for i in range(1,11,3):
#     print(i)
#
# #e.g.2
# a=int(input("start: "))
# b=int(input("stop: "))
# for i in range(a,b):
#     print(i)
#
# #e.g.3
# for i in range (10):
#     num1=int(input("num1: "))
#     num2=int(input("num2: "))
#     b=num1+num2
#     print("sum",b)
#
# #e.g.4
# for i in range(3):
#     num1=int(input("num1: "))
#     num2=int(input("num2: "))
#     b=num1*num2
#     print("product",b)
#     print("@"*30)
#
# #e.g.5
# sum=0
# for i in range(1,11):
#     sum+=i
#     print("current total",sum)
# print("total",sum)
#
#e.g.6
# s=[24,64,90,56]
# add=0
# for i in s:
#   add+=i
# print(add)
#
# for i in range(1,11):
#     if i%2==0:
#         print("the even number is",i)
#     else:
#         print("the odd number is",i)

# for i in range (25,326):
#   if even_number 1%2==0:
#     even_number+=1
#   else:
#     odd_number+=1


odd_count=0
even_count=0
for i in range (25,326):

  if i%2==0:
     even_count+=1
  else:
     odd_count+=1

     print(even_count)
     print(odd_count)

odd_sum=0
even_sum=0
for i in range (1,101):

  if i%2==0:
     even_sum+=i
  else:
     odd_sum+=i
     print("total"odd_sum)
     print(even_sum)