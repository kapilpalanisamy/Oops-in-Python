class User:

    def login(self):
        print("login")

    def register(self):
        print("register")

class Student(User):
    def enroll(self):
        print("enroll")

    def review(self):
        print("review")

stu1=Student()

stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
