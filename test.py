import random

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        # Generate a random 6-digit course ID
        self.Idnum = f"C{random.randint(100000, 999999)}"

    def display_idnum(self):
        print(f"Course ID for {self.course_name}: {self.Idnum}")

# Example Usage
course1 = Course("Introduction to Python")
course2 = Course("Data Structures")

course1.display_idnum()
course2.display_idnum()
print(course1.Idnum)  # You can also directly access the attribute if needed.