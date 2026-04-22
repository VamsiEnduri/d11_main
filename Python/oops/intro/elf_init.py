🔹 What is __init__ in Python?

__init__ is a special method (constructor) in Python.

👉 It runs automatically when you create an object

Example:
class Student:
    def __init__(self):
        print("Student object created")

s1 = Student()
Output:
Student object created

✔️ So whenever object is created → __init__ runs automatically

🔹 What is self?

self means 👉 current object

It is used to:

store data inside object
access object variables and methods
🔥 Real-Life Example

Think like this:

🏫 Class = Blueprint of a student
👨‍🎓 Object = Actual student (Vamsi, Ravi, etc.)

When a student joins:

__init__ → fills student details
self → represents THAT student
🔹 Example with self and __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Vamsi", 22)

print(s1.name)
print(s1.age)
Output:
Vamsi
22