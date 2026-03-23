import mysql.connector# connector which helps you to use connect() method

dbConnection=mysql.connector.connect( # db connect obj which creates connection to db in mysql
    host="localhost",
    user="root",
    password="10000Coders",
    database="sms"
)

print(dbConnection)
print("db connected successfully...")

curObj=dbConnection.cursor() #cursor object is to enabling to performing crud opertions

curObj.execute(
    """
create table if not exists students(
    id int primary key,
    name varchar(50) not null,
    age int,
    email varchar(30) unique not null 
)
"""
)


curObj.execute("select * from students")
allStuData=curObj.fetchall()

def dashboard(stud):
    # print(stud, "stud")

    print("1.edit yr profile")
    print("2.delete yr profile")
    print("3.view yr profile")

    o=input("choose option above :--  ")

    def deleteProfile(id):
        q="delete from students where id=%s"
        data=(id,)
        curObj.execute(q,data)
        dbConnection.commit()
        print("deleted successfully....")

    def viewProfile(id):
        q="select * from students where id=%s"
        data=(id,)

        curObj.execute(q,data)
        sData=curObj.fetchone()
        print("you got your data here ",sData)

    def editProfile(id):
        e=input("enter yr modified email here :--  ")
        curObj.execute("""
        update students
        set email=%s
        where id =%s
        
        """,(e,id))
        dbConnection.commit()
        print(f"student with {id} got updated")

    if o=="1":
        editProfile(stud[0])
        
    elif o=="2":
        deleteProfile(stud[0])
    else:
        viewProfile(stud[0])       

def register():
    n=input("enter name here :-- ")
    e=input("enter email here :--  ")
    a=int(input("enter age here :-- "))
    p=input("enter password here :-- ")
    cp=input("enter cpassword here :--  ")

    totalStudCount=len(allStuData) # [(),(),()]

    if p == cp :
        query="insert into students(id,name,age,email) values (%s,%s,%s,%s)"
        data=(totalStudCount+1,n,a,e)
        curObj.execute(query,data)
        dbConnection.commit()
        print("stu registered successfully.....")
        login()
    else:
        print("p and cp are not matching....")    

def login():
    curObj.execute("select * from students")
    allStuData=curObj.fetchall()
    print(allStuData,"allData at login func at 35 th line")
    nLogin=input("enter name here for login :-- ")
    eLogin=input("enter email here for email :-- ")
    for i in allStuData:
        if i [3] == eLogin: # "vamsi@gmail.com" == "ravi@gmail.com"
            if  i[1] == nLogin:
                print("login successful")
                dashboard(i)
            else :
                print("invalid cred") 
                break   
        else:
            print("stud not found")
            break    
    # for  i in allStuData:
    #     if i[1] == nLogin and i[3] == eLogin:
    #         print("login successful")
    #         dashboard(i)
    #     else:
    #         continue   


print("1.register")
print("2.login")
o=int(input("choose options above :---  "))
if o == 1:
    register()

if o == 2:
    login()    

 
# login()


     
        