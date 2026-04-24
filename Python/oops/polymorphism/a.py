# poly-morph-ism 
# will start in 2 mins 


# encapuslation 
# __pin=1234
# 3
# public self.pin :-- 
# protected self._pin :-- explore
# private self.__pin :--
# is it possible to access private data outside of class ? No :-- name mangling 
# what is name mangling ? :-- accessing private data with _classname__privateData
# how can we access privateData of a class ? using methods


# poly-morph-ism 
#  many - forms - process/technique


# class :-- methods  :-- 1 method :-- 2 args, 10 args 

def xyz():
    print("xyz function")  

class A:
    def __init__(self):
        pass 

    def abc(self,*arg): # load :-- 5 args  method overloading
        print(arg)
        print("abc method inside of class A")

o=A()
o.abc(10,20,10,123,234,"vamsi",True,[1,2,3,4],xyz())




# method overriding
class Animal:
    def Name(self):
        return "random name"


class Eagle(Animal):
    def Name(self):
        return "the king of sky"

o=Eagle()
res=o.Name()
print(res)




#  method overaloading :- a method can take n no of args 
#  is method over loading possible in python :-- no :-- *arg ( variable length args )
#  method overriding :-- suprpassing the parent method with child method with d/f behaviour
#  is method overriding possible in python without the inheritance ? no 