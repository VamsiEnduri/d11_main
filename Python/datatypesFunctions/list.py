# list :-- CRUD methods
#  create / add 
a=[1]
a.append(10) # [1,10] # adding one item at end
a.extend([11,12,13]) # [1,10,11,12,13] # adding multiple items at end
# print(a)

a.insert(0,"vamsi")
# print(a)
#  read 

# print(a)
# print(a[0])
# print(a[0:2]) # slicing # start
# print(a[len(a)-1])
# print(a[-1]) # negative indexing
# print(a[-1:-2:-1]) # slicing with negative direction (backward motion)
# #  update 
a[0]="ravi"

# print(a)


#  delete
# pop() :-- to remove item at end of list
# a.pop()
# pop(index) :-- to remove item based on index number
# a.pop(0)
# print(a)
# remove() :-- to remove item based on item name
# a.remove("ravi")
# print(a)

# print(a)
# del a 
# print(a)

# list + dict + str + tuple 