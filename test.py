import random
import time

class Person:
    def __init__(self, age, name, Idnum):
        self.age = age
        self.name = name
        self.Idnum = Idnum

    def birthday(self):
        self.age = self.age + 1

    def get_idnum(self):
        # This method can be used to retrieve the idnum
        return self.Idnum

    def set_idnum(self, new_idnum):
        # This is the "setter" method to update the idnum
        self.Idnum = new_idnum

ben = Person(31, "Ben", "123456")  # Pass idnum as an argument
paul = Person(42, "Paul", "987654")  # Pass idnum as an argument

print(ben.name, ben.age, ben.get_idnum())  # Use get_idnum to retrieve idnum
print(paul.name, paul.age, paul.get_idnum())  # Use get_idnum to retrieve idnum

while True:
  print("do you want to update ID numbers?")
  print("1. yes")
  print("2. no")

  choice = input("Enter your choice: ")

  if not choice.isdigit():
    print("Invalid input. Please enter a number.")
    time.sleep(2)
    continue

  choice = int(choice)

  if choice == 1:
      print("Who's ID number do you want to update?")
      print("1.", ben.name)
      print("2.", paul.name)
      person_choice = input("Enter your choice (1 or 2): ")

      if not person_choice.isdigit():
          print("Invalid input. Please enter a number.")
          time.sleep(2)
          continue

      person_choice = int(person_choice)

      if person_choice == 1 or person_choice == 2:
          new_idnum = input("Enter the new ID number: ")
          if person_choice == 1:
              ben.set_idnum(new_idnum)
              print(f"Updated {ben.name}'s ID number.")
              print(ben.name, ben.age, ben.get_idnum())
          elif person_choice == 2:
              paul.set_idnum(new_idnum)
              print(f"Updated {paul.name}'s ID number.")
              print(paul.name, paul.age, paul.get_idnum())
      else:
           print("Invalid input. Please select 1 or 2.")
           time.sleep(2)
  elif choice == 2:
      print("No IDs updated")
      break  # Exit the loop if the user chooses not to update
  else:
      print("Invalid choice. Please choose 1 or 2.")
      time.sleep(2)