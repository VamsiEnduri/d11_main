import mysql.connector


conObj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="10000Coders",
    database="d12"
)

curObj=conObj.cursor()
print("db connected successfully....")

# curObj.execute("""

# create table IF NOT EXISTS students(
#     id int ,
#     name varchar(50),
#     age int
# )

# """)


q="insert into students (id,name,age) values (%s,%s,%s)"

# data=(2,"akhil",29)
data = [
    (2, "akhil", 29),
    (3, "vamsi", 25),
    (4, "ravi", 22),
    (5, "suresh", 28)
]
# curObj.execute(q,data)
curObj.executemany(q,data) # query,data #opeart
conObj.commit() # PERM SAVE


q="select * from students"


curObj.execute(q)

allStuds=curObj.fetchall()
print(allStuds,"allstuds")

for i in allStuds:
    print(i)






t = ([1, 2], [3, 4])

t[0].append(99)

print(t)    