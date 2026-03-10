# #  functions - day 2

# # def details():
# #     name="ravi"
# #     age=27
# #     salary=77000
# #     print(f"hello my name is {name} and im {age} years old and im getting salary {salary}")
# # details()    


# name=input("enter yr name :-- ")
# email=input("enter yr email :-- ")
# password=input("enter yr password :-- ")
# c_password=input("enter yr c_password :-- ")

# def register(n,e,p,cp):
#     # print(n,e,p,cp)
#     if p == cp :
#         print(n,e,p,cp)
#         # db connection 
#         # db push
#     else:
#         print("p and cp must be matching")    

# register(name,email,password,c_password) # calling r invokation





# # def add(x,y,z): # params :-- params are nothing but the identifiers which takes the args while we pass during invokation


# # add(1,2,3) # values invokation calling arguments args   

# #  args are values which we pass to function at invkation time

#  function normal

# def details():
#     name="ravi"
#     age=27
#     salary=77000
#     print(f"hello my name is {name} and im {age} years old and im getting salary {salary}")
# details()  


# args + params function
# def abc(a,b,c):
#     print(a,b,c)
# abc(1,2,3)    

#  args + params + return keyword function


# def abc(a,b,c):
#     total=a+b+c
#     return total
# value=abc(1,2,3)  
# print(value)

# def xyz(a,b,c):
#     return [a,b,c,"vamsi","eagle"]
#     return a+b+c
# l=xyz(1,2,3)    
# print(l)


# 
# Variable Length Arguments (*args)

# def numbers(*x):
#     print(x)

# numbers(1,2,3,4,5) 

# Keyword Variable Length Arguments (**kwargs)

name=input("enter yr name :-- ") # vamsi
email=input("enter yr email :-- ") # "vamsi@gmail.com"
loc=input("loc here :-- ") #"hyd"
pin=input("pin here :-- ") #500072

def details(**keys):
    print(keys)

details(name=name,email=email,loc=loc,pin=pin)