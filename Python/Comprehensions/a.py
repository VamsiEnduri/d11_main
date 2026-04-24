# comprehensions  
# 👉 A short way to create lists using a single line of code instead of loops.

# syntax :-- 
# [expression for item in iterable]
# traditional for loop way
for i in [1,2,3,4,5]:
    if i %2 == 0:
        print(i**2)

#precise comprehension way
res=[i*i for i in [1,2,3,4,5] if i %2==0]
print(res)



# for loop-if-else in comprehension 
res=["even" if i % 2==0  else "odd" for i in [1,2,3,4,5]]
# print(res)


# if x<0:
#     print("negative")
# else:
#     if x == 0:
#         print("zero")
#     else:
#         print("postive number")      


# comprehsension with list with if-elif-else scenario
res= ["negative" if i<0 else   "zero"  if i==0  else "positive"   for i in [1,2,0,-9]]          
print(res)