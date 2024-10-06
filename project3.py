password="1234"
enter_password=input("enter your password: ")
while password != enter_password:
    print("incorrect password, please try again")
    enter_password=input("enter your password: ")
print("correct password,access granted")
