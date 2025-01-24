import random


class Person():
    def __init__(self, age, name, Idnum):
        self.age = age
        self.name = name
        self.Idnum = Idnum

    def birthday(self):
        self.age = self.age + 1  

    def get_idnum(self):
        # This method can be used to retrieve the idnum
        return self.Idnum


ben = Person(31, "Ben", "123456")  # Pass idnum as an argument
paul = Person(42, "Paul", "987654")  # Pass idnum as an argument
print(ben.name, ben.age, ben.get_idnum())  # Use get_idnum to retrieve idnum
print(paul.name, paul.age, paul.get_idnum())  # Use get_idnum to retrieve idnum

print("do you want to update ID numbers")
print("1.yes")
print("2.no")

if
  choice = input("Enter your choice: ")
  if not choice.isdigit():
    print("Invalid input. Please enter a number.")
    time.sleep(2)
    continue
  choice = int(choice)

  if choice == 1:
       print("who")
       print("1.", ben.name)
        print("2.", paul.name)
