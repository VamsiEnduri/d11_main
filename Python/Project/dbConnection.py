import mysql.connector
# pip install mysql-connector-python

cb_con_Obj=mysql.connector.connect(
    host="localhost",
    user="root",
    database="d11_oops_project",
    password="10000Coders"
)
# print(cb_con_Obj)

cur_obj=cb_con_Obj.cursor()