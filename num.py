import random

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        # Generate a random 6-digit course ID
        self.course_id = f"C{random.randint(100000, 999999)}"

    def display_course_id(self):
        print(f"Course ID for {self.course_name}: {self.course_id}")

# Example Usage
course1 = Course("Introduction to Python")
course2 = Course("Data Structures")

course1.display_course_id()
course2.display_course_id()
print(course1.course_id) # You can also directly access the attribute if needed.