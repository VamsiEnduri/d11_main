# acquiring the parent class attributes and methods by child class is called as inheritance

# accessing parent method with child class but outside of child class

# class A:
#     clName="pClass" # cls var r attribute

#     def surName(self): #defined method
#         # surName_="Enduri" # local var
#         self.surName_="Enduri" # instance var
#         print(self.surName_)

# class B(A):
#     clName="cClass" #cls var r attribute

#     def showDetails(self): #defined method
#         print("10000Coders")

# o=B()
# print(o.clName,"18")
# o.showDetails()
# o.surName()



#accessing parent method inside of the child class with super()

#  single level inheriatnce 
# class A:
#     clName="pClass" # cls var r attribute

#     def surName(self): #defined method
#         # surName_="Enduri" # local var
#         self.surName_="Enduri" # instance var
#         print(self.surName_)

# class B(A):
#     clName="cClass" #cls var r attribute

#     def showDetails(self): #defined method
#         print("10000Coders")
#         super().surName() # accessing parent method
#         print(super().clName) # accessing parent attribute

# o=B()
# o.showDetails()
# print(o.clName)




# ----- multi-level inheriatnce --------- 

class A:
    clName="AClass" # cls var r attribute

    def surName(self): #defined method
        # surName_="Enduri" # local var
        self.surName_="Enduri" # instance var
        print(self.surName_)

class B(A):
    clName="BClass" #cls var r attribute

    def showDetails(self): #defined method
        print("child B class and its parent is A and B is parent for child class C")
        super().surName() # accessing parent method
        print(super().clName) # accessing parent attribute

class C(B):
    clName="CClass"

    def showInfo(self):
        print("child c class and its parent is b")
        super().showDetails()
        print(super().clName)

o=C()

# print(o.clName) # 
# o.showInfo()



# CClass
# child c class and its parent is b
# child B class and its parent is A and B is parent for child class C
# Enduri
# AClass
# BClass



# -- multiple inheritance -- 

class A :
    clName="A" # attr
    
    def height(self): # method
        self.height__=5.6
        print(self.height__)

class B:
    clName="B" # attr

    def __init__(self,clr):
        self.color=clr

    def skinColor(self): #method
        # self.color="white"
        print(self.color)

class C(A,B):
    clName="C" # child attr

    def __init__(self,n,clr,he): # child method
        self.name = n
        abc=super().clName
        super().__init__(clr) 
        super().__init__(he)

    def acquireChars(self):
        print(self.color)
        # super().skinColor()
        # super().height()

# o=C("vamsi","white",5.6) # 
# o.acquireChars()



# -- hierarchial inheritance -- 



class A :
    clName="A" # attr
    
    def height(self): # method
        self.height__=5.6
        print(self.height__)


class A1(A):
    childName="A1"

    def acquireChars(self):
        super().height()

o1=A1()
o11=A1()
o1.acquireChars()

class A2(A):
    childName="A2"

    def acquireChars(self):
        super().height()
        
o2=A2()   
o2. acquireChars()    



