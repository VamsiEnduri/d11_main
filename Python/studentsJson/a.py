# # # #  json :-- [{},{}] :-- text :-- for i in data:
# # # # client          server
# # # a=[{"id":1,"name":"vamsi"},{"id":2,"name":"ravi"}] #list of dicts python code
# # # # json format :-- str 

import json
data=[{"name": "akhil", "age": 29}, {"name": "srinu", "age": 22}]
print(type(data))
abc=json.dumps(data) #json str
print(type(abc))
xyz=json.loads(abc)
print(type(xyz))

# # # # json format :-- str :
# # # # python list of dicts

# # import json 


# # # reading 
# # abc=open("students.json","r")

# # resData=json.load(abc) # allstuds

# # # adding new stud

# # new_data={"id":3,"name":"rakesh"} # new_stud
# # resData.append(new_data) # [{},{},{}]
# # xyz=open("students.json","w")

# # json.dump(resData,xyz)

# import json

# print("1. adding student")
# print("2. reading students")
# print("3. updating student")
# print("4. deleting student")
# print("5.  exit")

# file_name="students.json"
# def load_data():
#     abc=open("students.json","r")
#     return json.load(abc) #[]

# def dump_data(x):
#     xyz=open(file_name,"w")
#     json.dump(x,xyz)


# def add_student():
#     allstuds=load_data()
#     n=input("enter name here :-- ")
#     a=int(input("enter age here :-- "))

#     new_data={"name":n,"age":a}
#     allstuds.append(new_data)

#     dump_data(allstuds)

#     print("student added successfully....")
#     # [].append(new_data)


# def view_students():
#     allStuds=load_data()
#     # for i in allStuds:
#     #     print(i["name"], i["age"])
#     for i in range(0,len(allStuds)):
#         print(i+1,allStuds[i]["name"], allStuds[i]["age"])


# def update_student():
#     allStuds=load_data()
#     view_students()
#     i=int(input("enter id to update the student :--   "))
#     name=input("enter name here :-- ")
#     age=int(input("enter age here "))
#     indexNum=i-1
#     allStuds[indexNum]={"name":name,"age":age}
#     dump_data(allStuds)
#     print("student got updated....")

# def delete_student():
#     allStuds=load_data() #data #[{},{},{}]
#     view_students()# display
#     i=int(input("enter studnet id to dlete :--  ")) # 3
#     indexNum=i-1 # 3-1 = 2
#     allStuds.pop(indexNum) # #[{},{}]
#     dump_data(allStuds)
#     print(f"student got dleted whose having id {i}")


# while True:
#     o=int(input("enter option here fro above list :--  "))
#     if o==1:
#         add_student()
#     elif o == 2:
#         view_students()  
#     elif o ==3:
#         update_student()  
#     elif o == 4:
#         delete_student() 
#     else:
#         break;           