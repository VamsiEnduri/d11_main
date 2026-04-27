class DashBoard:
    def __init__(self,i):
        print("dashboard")
        print(i)

        while True :
            print("explore customer features - HDFC BANK")
            print("1. withdraw")
            print("2. deposit")
            print("3. check_bal")
            print("4. exit")


            o = int(input("Enter option: "))

            if o == 1:
                from dbConnection import cur_obj,cb_con_Obj
                p=input("enter password to withdraw the amount")
                a=int(input("enter amount to draw here :-- "))
                def withdraw(incomingP,withdrawAmt):
                    nonlocal i

                    if incomingP == i[len(i)-1]:
                        if withdrawAmt <=0:
                            print("enter valid amount ")
                        else:
                            if withdrawAmt < i[3]: # 1000 < 860
                                i=list(i)
                                i[3] -= withdrawAmt 
                                return i[3] 
                            else:
                                print(f"insuffcient funds :-- yr bal is {i[3]}")
                                return "insuffcint funds"    
                    else:
                        print("wrong pin ")
                rem_bal=withdraw(p,a)  
                q="update users set balance=%s where acc_num=%s and password= %s"
                d=(rem_bal,i[2],p)
                cur_obj.execute(q,d)
                cb_con_Obj.commit()
                print(f"remaining bal is {rem_bal} and withdrawan amount is {a}")         
            elif o == 2:
                print("deposit feature")
            
            elif o == 3:
                p=input("enter password to check the bal")
                def check_bal(incomingP):
                    if incomingP == i[len(i)-1] :
                        # print(self.__balance)
                        return i[3]
                    else:
                        print("enter proper pin to proceed furthur")
                bal=check_bal(p)
                print(f"main bal is {bal}")
            elif o == 4:
                break 
                # pass         