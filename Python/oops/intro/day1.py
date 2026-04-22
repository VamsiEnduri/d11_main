# # # a=10
# # # print(type(a))
# # # def abc():
# # #     #
# # #     pass
# # # print(type(abc))   
# # # import math
# # # print(math.sqrt)

# # # syntax 
# # # class cl_name:
# # #     #class code
# # #     #class code
# # #     #class code
# # #     #class code
# # #     #class code
# # #     #class code
# # # obj=cl_name()    
# # # print(obj)
# # abc=100 #global var
# # class A:
# #     print("vamsi")
# #     className="A" # class  var
# #     print(className)
# #     def abcdef():
# #         print("abcdef")
# #         x=200 #local var
# #         y=300 #local var
# #         print(x+y)
# #     abcdef()    
# # o=A()  
# # print(o.className,"outside")

# # # print(object)  


# # oops 
# # why oops ?
# # pillars ?
# # class 
# # obj creation 
# # class variables
# # class lo , function (method)

# class Student: # creating class / creating blueprint
#     cl_name="student" # cls variable # varaibles

#     def details(): #methods
#         print("print details")
        
# Student() # creating object        


# abc




class Student: # creating class / creating blueprint
    cl_name="student" # cls variable # varaibles

    def details(x,name,age,location): #methods
        x.n = "vamsiEnduri"
        x.a=age
        x.loc=location
        print(o.n,x.a,x.loc)      
        
o=Student() # creating object 
print(o.cl_name)
o.details("vamsi",27,"hyd")
print(o.n)
print(o.a)
print(o.loc)




class student:
    cl_name="student" # cls variable
    
    def __init__(self,i,b,n,a): # default method
        self.name = n 
        self.age= a 
        self.batch=b 
        self.institute = i
        print(self.institute,self.batch,self.area)
        print("default construction function")

    def details(self,a):
        self.area = a 
        print("details function")
        print(self.name,self.age,self.batch,self.institute,"details")

o=student("10000coders","d11","vamsi",27)   #obj creation     
o.details("kphb hyd") 
print(o.name,o.age,o.batch,o.institute)  