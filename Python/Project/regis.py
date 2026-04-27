
from dbConnection import cur_obj,cb_con_Obj
from login import Login

class Register__:

    def __init__(self,n,ac_num,fst_bal):
        queryTableCreation="""
        create table if not exists users(
        customer_id int primary key auto_increment,
        name varchar(50) not null unique,
        acc_num varchar(16) not null,
        balance decimal(10,2) not null,
        password varchar(16) not null
        )
        """
        cur_obj.execute(queryTableCreation)
        p=input("enter password here :-- ")
        c_p=input("enter password again here :-- ")
        if p == c_p:
            q="insert into users(name,acc_num,balance,password) values (%s,%s,%s,%s)"
            d=(n,ac_num,fst_bal,p)
            cur_obj.execute(q,d)
            cb_con_Obj.commit()
            print("user registered successfully") 

            if True :
                accNumber_input_Login=input("enter your acc_number :--- ")
                p_Login=input("enter password here :-- ")
                Login(accNumber_input_Login,p_Login)




name = input("Enter name: ")
acc = input("Enter acc no: ")
bal = input("Enter balance: ")

Register__(name, acc, bal)

 # object creation     