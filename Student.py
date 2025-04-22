class Student:
    student_count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = Student.student_count + 1
        Student.student_count += 1

    def introduce(self):
        print(f"Hi, my name is {self.name} , I am {self.age} years old and my student ID is {self.id}")

    @classmethod
    def total_students(cls):
        print(f"Total students enrolled: {cls.student_count}")

s1 = Student("Yahmin" , 20)
s2 = Student("Mukelwa" , 15)

s1.introduce()
s2.introduce()

Student.total_students()

class Prefect(Student):
    pass

s3 = Prefect("Selu" , 19)
s3.introduce()