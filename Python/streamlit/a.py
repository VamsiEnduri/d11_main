import streamlit as st
import mysql.connector
print(st)

dbConnection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="10000Coders",
    database="d11__"
)

curObj=dbConnection.cursor(dictionary=True)

print("db connected successfully....")

st.title("hello welcome to SMS portal")

options=st.sidebar.selectbox("choose operation",["c","r","u","d"])

if options == "c":
    st.subheader("Add New Student 📝")
    with st.form("creating student"):
        curObj.execute("SELECT id, name FROM studs")  # get ID and Name
        students = curObj.fetchall()
        name=st.text_input("name")
        age=st.number_input("age",min_value=18,max_value=35,step=1)
        btn=st.form_submit_button("add student")

        if btn:
            q="insert into studs(id,name,age) values (%s,%s,%s)"
            data=(len(students)+1,name,age)
            curObj.execute(q,data)
            dbConnection.commit()
            st.success(f"student {name} added successfully to table")
elif options == "r":
    st.subheader("read Students 📝")
    q="select * from studs"
    curObj.execute(q)
    allStuds=curObj.fetchall()

    if allStuds:
        st.dataframe(allStuds)
    else:
        st.info("no students found")    
elif options == "d":
    curObj.execute("SELECT id, name FROM studs")  # get ID and Name
    students = curObj.fetchall()
    print(students,"students")
    st.subheader("Delete Student 📝")
    stu_dicts={}
    for i in students:
        key=i["name"]
        stu_dicts[key]=i["id"] #{"vamsi":1},{"ravi":2}

    print(stu_dicts,"all stud dict")
    with st.form("deleting studnet"):
        stu=st.selectbox("choose student to dlete",list(stu_dicts)) #"vamsi"
        btn=st.form_submit_button("delete student")
        print(stu,"deleted stud")

        deletable_stud=stu_dicts[stu] #{"vamsi":1} #1

        if btn:
            q="delete from studs where id=%s"
            data=(deletable_stud,)
            curObj.execute(q,data)
            dbConnection.commit()
            st.success("student deted successfully....")

