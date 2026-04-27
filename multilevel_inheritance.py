class School:
    def __init__(self,school_name):
        self.school_name = school_name
    
    def show_school(self):
        print("Name of the School is", self.school_name)
    
class Teacher(School):
    def __init__(self,school_name,teacher_name,subject):
        super().__init__(school_name)
        self.teacher_name = teacher_name
        self.subject = subject
    
    def show_teacher(self):
        print("Teacher Details")
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)

class Student(Teacher):
    def __init__(self,school_name,teacher_name,subject,student_name,grade):
        super().__init__(school_name,teacher_name,subject)
        self.student_name = student_name 
        self.grade = grade 
    
    def show_details(self):
        print("Student DEtails")
        print("Student Name:", self.student_name)
        print("Student Grade:", self.grade)
    
st1 = Student("Alvas High School","Anushree","Science","Divya","B")
st1.show_details()
st1.show_teacher()
st1.show_school()

st2 = Student("Bharathi High School","Divyashree","Mathematics","Aquila","A")
st2.show_details()
st2.show_teacher()
st2.show_school()
