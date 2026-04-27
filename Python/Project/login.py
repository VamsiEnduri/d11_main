from dbConnection import cur_obj,cb_con_Obj

class Login:
    def __init__(self,an,p):
        queryToFetchData="select *from users"
        cur_obj.execute(queryToFetchData)
        usersData=cur_obj.fetchall()
        
        for i in usersData:
            if i[2] == an and i[4] == p:
                from dashboard import DashBoard
                DashBoard(i)
                break
            else:
                print("customer not found with that details")
                continue    
        
        print("login class ")


acc = input("Enter acc no: ")
pwd = input("Enter password: ")
Login(acc, pwd)
# Login()
    