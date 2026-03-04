# # # abc=10 # assigning
# # # abc="vamsi" # re-assigning

# # # # data 


# # # primitive:
# # name="vamsi" # 01234
# # # we can access the chars in str by using realtive index numbers 

# # # len(name) # 5
# # # print(name)
# # print(name[2],len(name))

# # # no-primitive
# # # list  # ordered data
# # alphas=["a","b","c","d","e"]  #01234
# # # len(numbers) # 5
# # # print(numbers)
# # print(alphas[len(alphas)-1]) # alphas[5-1] alphas[4] # e
# # t=("ntr","ram","prabhas","aa")

# # d={"id":1,"name":"vamsi"}
# # # dict
# # # we can access the items in the list by using realtive index numbers 

# # a=10
# # typeof(a) # im finding what type of data that a is 

# a=10
# b="vamsi"
# c=[1]
# d={"id":1}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# a=input("enter your name :--    ") # input() data default str treat by interpreter
# print(a)
# print(type(a))
name=input("enter your name :-- ")
age=int(input("enter your age :-- ")) # int("27") age=27
salary=float(input("enter your salary :-- "))
print(name)
print(age)
print(salary)
print(name+age+salary)

# research topics :
str()
bool()