# # Check Even or Odd
# # num=int(input("enter number here :--  "))
# # def check_even_odd(x):
# #     if x % 2 == 0:
# #         print(x,"is even num")
# #     else:
# #         print(x,"is odd num")    

# # check_even_odd(num) 


# # Check Even numbers or Odd numbers from m - n 

# # a=10
# # print(a1)

# num1=int(input("enter number 1 here :--  "))
# num2=int(input("enter number 2 here :--  "))
# def check_even_odd(x,y):
#     totalProEvn=1
#     totalProOdd=1
#     for i in range(x,y+1):
#         if i % 2 == 0:
#             # print(i,"is even num")  
#             totalProEvn*=i
#         else:
#             totalProOdd*=i
                
#     print(totalProEvn,"totalEvn")
#     print(totalProOdd,"totalOdd")
# check_even_odd(num1,num2) 

# Biggest Among Two Numbers
# num1=int(input("enter number 1 here :--  "))
# num2=int(input("enter number 2 here :--  "))

# def findingBiggestNumberB2(x,y): # 10 , # 5
#     if x > y : # 10 > 5
#         print(x,"is big number") 
#     else:
#         print(y,"is big number")       
# findingBiggestNumberB2(num1,num2)    



# smallest Among Two Numbers

# num1=int(input("enter number 1 here :--  "))
# num2=int(input("enter number 2 here :--  "))

# def findingSmallestNumberB2(x,y): 
#     if x < y : 
#         print(x,"is small number") 
#     else:
#         print(y,"is small number")       
# findingSmallestNumberB2(num1,num2)   



# num=int(input("enter number 1 here :--  "))


# def findingdivBy5notby10(x):

#     if x % 5 == 0 and x % 10 != 0: # True and True
#         print(x,"is div by 5 and div not by 10")
#     else:
#         print(x,"is lllllll")    


# findingdivBy5notby10(num)



# num=int(input("enter number 1 here :--  "))

# def findingNumdivBy2_3_6(x):

#     if x % 2 == 0 and x  % 3 == 0 and x % 6 == 0:
#         print(x,"is div by 2 3 6 ")
#     else:
#         print(x,"is not div by all 2 and 3 and 5 it fails someherwe to get divid by")    


# findingNumdivBy2_3_6(num)




#  Biggest Among Three Numbers

# num1=int(input("enter number 1 here :--  "))
# num2=int(input("enter number 2 here :--  "))
# num3=int(input("enter number 3 here :--  "))

# def b(x,y,z):

#     if x > y and x >z:
#         print(x,"is big number")
#     elif y > x and y > z:
#         print(y,"is b number")
#     else:
#         print(z, "is b bumber")        
# b(num1,num2,num3)   




#  Print Factors of a Number
# 10 :--
# 1, 10, 2 , 5

# 2:-
# 1,2

# 3:-- 1,3


# num=int(input("enter a num here "))
# factors=[]

# def findingFactors(x):
#     count=0
#     for i in range(1,x+1):
#         if x % i == 0:
#             count+=1
#             print(i,"is factor for",x) # 
#             factors.append(i)
#     print(count)        

# findingFactors(num)
# print(factors)


# n ! factorail of number

# num=int(input("enter a num here "))


# def factorail(x):
#     fact=1
#     for i in range(x,0,-1):
#         fact*=i
#     print(fact) 
# factorail(num)   



# python errors :-- 15+

# before code execution starts :--  syntax error, indention error
# errors while executing lines :--  key error, attribute error, local bound error, etc.. typeerror, nameerror



1a=10
    b=20
print(1a+b)    


a=10

b=20

def abc():
    pass
abc()

abcd=100
print(xyz)

