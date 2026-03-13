a=10
print(a)

# scope :--the area in which you access a varaible is called as scope
# what is scope of varaible a in line 1:-- ans :-- total entire file 
# why ? global varaible :-- globally accessable



def add():
    print(a)
    x=10 # the scope of x is ? only in the block of add function
    y=20
    print()
    print(x+y)
add()    
print()

def mul():
    print(a)
    a=100 # in mul function block itself
    b=2 # mul func block only :-- scope
    print(a*b)
mul()

# what is the function scoped variable here in the file ? mention any two ?
# LEGB :-- legb
print(a)

























































































print(a)