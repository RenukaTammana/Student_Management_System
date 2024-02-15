class Student:
    def __init__(self,id_no,name):
        self.id_no = id_no
        self.name = name
        self.enrolled ={}
    def enroll(self,course,marks=0):
        self.enrolled[course] = marks
    def get_courses(self):
        return self.enrolled.keys()
    def get_marks(self):
        return self.enrolled.values()
    def __str__(self):
        return f"Student_ID:{self.id_no} Name: {self.name} "
class Course:
    def __init__(self,c_id,course):
        self.c_id = c_id
        self.course = course
    def __str__(self):
        return f"Course_Id: {self.c_id} Course: {self.course}"
class Grades:
    def cal_gpa(marks):
        if not marks:
            return 0.0
        p = 0
        for i in marks:
            if i>90:
                p+=10
            elif i>80 and i<=90:
                p+=9
            elif i>70 and i<=80:
                p+=8
            elif i>60 and i<=70:
                p+=7
            elif i>50 and i<=60:
                p+=6
            else:
                p+=5
        return p/len(marks)
s1 = Student(597,"Roy")
s2 = Student(589,"John")
c1 = Course("21CS01","Oops through Java")
c2 = Course("21CS02","Core Programming with Python")
c3 = Course("21CS03","Computer Networks")
c4 = Course("21CS04","Cryptography")
s1.enroll(c1,90)
s1.enroll(c2,67)
s2.enroll(c1,78)
s2.enroll(c3,56)
print(s1)
print(f"Enrolled courses: {[str(i) for i in s1.get_courses()]}")
print(f"Marks: {s1.get_marks()}")
print(f"GPA: {Grades.cal_gpa(s1.get_marks())}")
print()
print(s2)
print(f"Enrolled courses: {[str(i) for i in s2.get_courses()]}")
print(f"Marks: {s2.get_marks()}")
print(f"GPA: {Grades.cal_gpa(s2.get_marks())}")