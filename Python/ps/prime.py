# # prime :-- 2 3 5 ----------
# # 1*2 = 2
# # 2*1 = 2

# # 1*3 = 3
# # 3*1 = 3

# # 1*4 = 4
# # 4*1 = 4
# # 2*2 = 4

# # 1*5 = 5 
# # 5*1 = 5

# # 1*6=6
# # 6*1=6
# # 3*2=6
# # 2*3=6


# # 1* 7 = 7
# # 7*1 = 7


# # prime numbers :-- 
# # if a number can be called as prime :
# #     that number should be factor of that number 
# #     that number itself is a factor



# num=int(input("enter a number :-- ")) # 11
# count=0
# if num>=1:
#     for i in  range(1,num+1): # 2 3 4 5 6 7 8 9 10
#         if num % i == 0 :# 11 % 2
#             count+=1
# else:
#     print("<=1 are not considered as prime numbers")    

# print(count,"count")
# if count == 2:
#     print(num,"it is prime")
# else:
#     print("it is not prime")    



# # num=int(input("enter a number :-- ")) # 2
# # count=2
# # if num>1: # 2>1
# #     for i in  range(2,num): # 2 , 2
# #         if num % i == 0: # 2 % 2  == 0 
# #             count+=1    # 3
# #             break
# # else:
# #     print("<=1 are not considered as prime numbers")    

# # if count ==2:
# #     print("prim")
# # else:
# #     print("not prime")     



# finding prime numbers in range of 1-10

# 1 4
# 2 4
# 23

start=int(input("enetr start range ")) # 1
end=int(input("enetr end range ")) # 2
count =2
pnumbers=[]
for i in range(start,end+1): #i= 11
    if i>1: #4  # 11>1       
        count =2 #2
        for j in range(2,i):
            if i % j == 0 :
                count+=1
                break 
        if count == 2:
            # print("prime")
            pnumbers.append(i)
        else:
            pass        
    else:
        print("<= 1 are not prime numbers")
print(pnumbers)
       

