# #exceptional handling ( error handling )

# # try:
# #     salary=int(input("enter salary here :-- "))
# #     bonus=5000 # breadcrumbs
# #     totalSalary=salary+bonus
# #     print(totalSalary)
# # except :
# #     print("you are not supposed to give other datatype to int () function except str int")
# #     #code

# # def login():
# #     print("login done")
# # login() 



# try:
#     salary=int(input("enter salary here :-- "))
#     bonus=5000 # breadcrumbs
#     totalSalary=salary+bonus
#     print(totalSalary)
# except :
#     print("you are not supposed to give other datatype to int () function except str int")
#     #code


# try:
#     a=10
#     print(a1)
# except:
#     print("cant try access to names which are not defined ")    

# # a=10
# # print(a1) #nameerror

# print("line after 35 i.e im 36 line")
# try:
#     a={"id":1}
#     print(a["name"])
# except:
#     print("this exception :-- try to access the key which are inside the dict 39 line")    


try:
    #code
    a=10
    print(a) #nameerror

except NameError:
    print("cant try access to names which are not defined ")   

except ValueError:
    print("you are not supposed to give other datatype to int () function except str int")

except TypeError:
    print("this exception :-- try to access the key which are inside the dict 39 line")
    
else:
    print("all good")  

finally:
    print("i will execute anyway")





