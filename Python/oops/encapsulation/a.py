#  encapuslation 
#  is a technique in oops which is used to hide the data from accessing anywehere in the class like class varaibles r instance varaibles



# example :-- 
# class student:
#     cl_name="student" # cls variable
    
#     def __init__(self,i,b,n,a): # default method
#         self.name = n 
#         self.age= a 
#         self.batch=b 
#         self.institute = i
#         print(self.institute,self.batch,self.area)
#         print("default construction function")

#     def details(self,a):
#         self.area = a 
#         print("details function")
#         print(self.name,self.age,self.batch,self.institute,"details")

# o=student("10000coders","d11","vamsi",27)   #obj creation     
# o.details("kphb hyd") 
# print(o.name,o.age,o.batch,o.institute) 



class Bank:
    bankName="HDFC"

    def __init__(self):
        self.branch="KPHB"
        self.pincode=500072
        self.__pin=1310 # private 
        self.__balance=860 # private

    def accessDetails(self):
        print(self.branch)
        print(self.pincode)

    def check_bal(self,incomingPin):
        if incomingPin == self.__pin :
            # print(self.__balance)
            return self.__balance
        else:
            print("enter proper pin to proceed furthur")

    def withdraw(self,incomingPin,withdrawAmt):
        if incomingPin == self.__pin :
            if withdrawAmt <=0:
                print("enter valid amount ")
            else:
                if withdrawAmt < self.__balance: # 1000 < 860
                    self.__balance -= withdrawAmt 
                    return self.__balance   
                else:
                    print(f"insuffcient funds :-- yr bal is {self.__balance}")
                    return "insuffcint funds"    
        else:
            print("wrong pin ")

            
    def deposit(self):
        pass             

o=Bank() 
# bal=o.check_bal(int(input("enter yr pin to get bal details ...")))
# print(bal)
wAmt=o.withdraw(int(input("enter yr pin to proceed for withdrawal of amt ...")),int(input("enter amount to draw... ...")))
print(wAmt,"wamt")
# o.accessDetails() 
# print(o.pincode,"44")
# print(o._Bank__pin,"45") # cant be accessible outside of class due to they are private var

#name mangling


# public accessable varaibles self.pin
# protected varaibles self._pin
# private variables    self.__pin   # -------------------------


# kphb
# 500072