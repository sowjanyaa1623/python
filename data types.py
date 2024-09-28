# print("hi guys")
# print("first class")
#
# #data types
# #integer
# #float
# #string
#
# sowjanyaa=100
# print(sowjanyaa)
# print("sowjanyaa")
# VALUE = 10
# l=True
# x=50,32,1.7
# print(x)
# print(VALUE)
# print(l)
#
# #keyword-special
# #if,else,and,True,False,in,for,.....
#
# """Identififiers-names given to my variables
# it has to start with alphabet or (_)
# it may contain numbers
# it should not contain any white spaces
# it should not be a keyword
# it should not contain any special characters"""
#
# _name="cat"
# print(_name)
# value=144
# print(value)
# age_of_sowjanyaa=13
# print(age_of_sowjanyaa)
# rank="eight"
# print(rank)
#
# #commenting
# #1.Single line commenting-#
# #2.Multi line commenting-"""....."""
#
# #type function
# height=157.9
# print(type(height))#class float
# x=57
# print(type(x))#class integer
# a=("apple")
# print(type(a))#class str
# l=True
# print(type(l))#class bool

# #type conversion
# #explicit type conversions
# #int---float
# ice=35
# print(ice)#35
# print(type(ice))#int
# print(float(ice))#35.0
# ice=float(ice)#35----35.0
# print(ice)#35.0
# print(type(ice))#float

# #int----str
# x=24
# print(type(ice))#int
# print(str(x))#24
# s=str(x)#24-----"24"
# print(x)#24
# print(type(ice))#str

# #int----bool
# l=50
# print(type(l))#int
# print(bool(l))#true
# l=bool(l)#50----True
# print(l)#True
# print(type(l))#bool

# y=0
# print(type(y))#int
# print(bool(y))#False
# y=bool(y)#0-----False
# print(y)#False
# print(type(y))#bool

# #float---integer
# r=45.0
# print(type(r))#float
# print(int(r))#45
# r=int(r)#45.0----45
# print(r)#45
# print(type(r))#int

# #float---str
# s=5.4
# print(type(s))#float
# print(str(s))#5.4----"5.4"
# s=str(s)#5.4
# print(s)#5.4
# print(type(s))#5.4

# #float---bool
# k=24.3
# print(type(k))#float
# print(bool(k))#True
# k=bool(k)#24.3----True
# print(k)#true
# print(type(k))#bool

# #str----int
# z="48"
# print(type(z))#srt
# print(int(z))#48
# z=int(z)#"48"---48
# print(z)#48
# print(type(z))#int

# #str----float
# u="3.5"
# print(type(u))#str
# print(float(u))#3.5
# u=float(u)#"3.5"---3.5
# print(u)#3.5
# print(type(u))#float

# #str----bool
# w="lion"
# print(type(w))#str
# print(bool(w))#True
# w=bool(w)#"lion"---True
# print(w)#True
# print(type(w))#bool

# v=""#None(or)""
# print(type(v))#str
# print(bool(v))#False
# v=bool(v)#""----False
# print(v)#False
# print(type(v))#bool

# #bool----int
# c=False
# print(int(c))#0
# print(float(c))#0.0
# print(str(c))#False

# j=True
# print(int(j))#1
# print(float(j))#1.0
# print(str(j))#True

# #implicit conversions
# a=8
# b=6.5
# c=a+b
# print(c)#14.5
# print(type(c))#float

# #user-defined input

# #input()-----string
# value=input("enter a value: ")
# print(value)
# print(type(value))
#
# #input()-----int
# value1=int(input("value1: "))
# print(type(value1))
#
# #float(input())----float
# value2=float(input("value2: "))
# print(value2)

#bool(input())
value3=bool(input("value3: "))
print(value3)
print(type(value3))

# #get the name, age and weight of your family member
# name=input("enter your name: ")
# print(str(name))
# age=input("enter your age: ")
# print(int(age))
# weight=input("enter your weight: ")
# print(float(weight))

#arithmetic operater(+,-,*,/,//,**)
# a=9
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
#
# #assignment operations(=,+=,-=,*=,/=,//=,%=,**=)
# cat=30
# print(cat)
# cat+=5
# print(cat)
# cat*=3
# print(cat)
# cat-=6
# print(cat)


#seperative
# y_name=input("enter y's name:  ")
# x_name=input("enter x's name:  ")
# z_name=input("enter z's name:  ")
# print(y_name,x_name,z_name,sep="-")
#
# #end parameter
# print("password",end=":")
# print("1234")