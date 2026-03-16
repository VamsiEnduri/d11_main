# # global 
# name="vamsi"
# email="vamsi@gmail.com"
# password="12345678"
# c_password="12345678"


# print("1.  do register")
# print("2.  do login")


# c=input("choose one option")
# email="v"
# eamil="vp"

# def credChange():
#     print("cred chnage function invoked")
#     global email
#     email=input("enter your updating email here :--  ")
#     global password
#     password=input("enter your new password here :--   ")

#     print(email,password,"22 line") # new email, password


# def login():
#     emailL=input("enter yr email @login :-- ") # "vamsi@gmail.com"
#     passwordL=input("enter yr password @login:-- ")
#     if emailL == email and passwordL == password:
#         dashboard(name)
#     else:
#         print("invalid credentials")

# def dashboard(name):
#     print(f"welocme {name}")
#     print("1. search feed")
#     print("2. upload reel")
#     print("3. account")

#     c=input("choose one option above :-- ")

#     if c=="1":
#         pass 
#     elif c=="2"    :
#         pass
#     elif c=="3":
#         print("1.account settings")
#         print("2. edit profile")

#         c=input("choose one :--   ") 

#         if c=="2":
#             print("edit profile need to be called")
#             credChange()

               
 




# if c=="1":
#     name=input("enter yr name :-- ")
#     email=input("enter yr email :-- ")
#     password=input("enter yr password :-- ")
#     c_password=input("enter yr c_password :-- ")

#     def register(n,e,p,cp):
#     # print(n,e,p,cp)
#         if p == cp :
#             print(n,e,p,cp)
#         # db connection 
#         # db push
#         else:
#             print("p and cp must be matching")    

#     register(name,email,password,c_password) # calling r invokation
# elif c == "2":
#     login()    

   


# # nonlocal 


def outer():
    oVar="outer"
    
    def inner():
        iVar="inner"
        nonlocal oVar
        oVar="10000Coders"


        def deepInnerMost():
            dmVar="deepMostVar"
            nonlocal oVar
            oVar="vamsi"

        deepInnerMost() 

    inner()

    print(oVar,"102") # 10000Coders
outer()