# # # #  logical operators 
# # # # and true and true
# # # # or true or false
# # # # not  vice-versa opposite

# # # # and 

# # # abc=10 == 10 and 20 == 10
# # # print(abc,"and")

# # # #  or 

# # # abc=10 == 10 or 20 == 10
# # # print(abc,"or")

# # # #  not 
# # # abc=not (10 == 10 or 20 == 10)
# # # print(abc,"not")



# # #  memebership 
# # # check weather the item is member of that seq of items or not
# # # in can workon seq/range
# # "a" in "vamsi" # True
# # 1 in [1,2,3] # True
# # "banana" in ("banana","apple") #True
# # 3 in range(1,11) #True
# # "a" in "srinu" # False
# # "banana" in ("orange","apple") #False

# # # not in
# # "a" not in "srinu" #True
# # "banana" not in ("orange","apple") # True


# # primtive immutable
# # name="vamsi"
# # name[0]="E"
# # print(name[0])
# # # non-p mutable
# # 0="ntr"
# # 0="vamsi"
# # item re-assignment
# # heros=["ntr","rc","aa","mb"]
# # print(heros[0])
# # heros[0]="vamsi" #["vamsi","rc","aa","mb"]
# # print(heros) # #["vamsi","rc","aa","mb"]
# # heros[len(heros)-1]="srinu"
# # print(heros)


# d={
#     "id":1,
#     "name":"vamsi" # item
# }
# # print(d["name"]) #"vamsi"
# d["name"]="ntr"
# print(d)


# a=(1,2,3)
# a[0]="vamsi"
# print(a)



# # conditional statements in python :--
# statements -- lines
#  conditional statements  -- 

# if syntax

# if condition :
#     print("true condition")

# if True:
#     print("yes 10 is equal to 10")
#     print("yes 10 is equal to 10")
#     print("yes 10 is equal to 10")
#     print("yes 10 is equal to 10")
#     print("yes 10 is equal to 10")
#     print("yes 10 is equal to 10")
# print(100)


# if-else
name="vamsi__"
pswd="12345678"

n=input("enter name here :-- ")
p=input("enter password here :-- ")

if name == n and pswd == p :
    print("login successful......")
else:
    print("invalid credentials")    
