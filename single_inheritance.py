class Course:
    def __init__(self,course_name, price):
        self.course_name = course_name
        self.price = price
    
    def show_course():
        print("Course Name:", self.course_name)
        print("Price:",self.price)
        
class ProgrammingCourse(Course):
    def __init__(self, course_name, price,  language, duration):
        super().__init__(course_name, price)
        self.language = language
        self. duration = duration
    
    def show_programming_course():
        super().show_course()
        print("Language:", self.language)
        print("Duration:", self.duration)
        
co1 = ProgrammingCourse("Data Science", 35000, "Python", "7 months")
co2 = ProgrammingCourse("Java Mastery", 20000, "Java", "5 Months")

co1.show_programming_course()
co2.show_programming_course()
