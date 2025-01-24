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
        return self.Idnum

    def set_idnum(self, new_idnum):
        self.Idnum = new_idnum
        
    def __str__(self): # added for better printing
        return f"Name: {self.name}, Age: {self.age}, ID: {self.Idnum}"

# Store Person objects in a list
people = [
    Person(31, "Ben", "123456"),
    Person(42, "Paul", "987654"),
    Person(22, "Sarah", "456789"), #additional person to test scalability
    Person(60, "John", "789012")  #additional person to test scalability
]

# Initial print of the persons
for person in people:
  print(person)

while True:
    print("\nDo you want to update ID numbers?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(2)
        continue

    if choice == 1:
        print("Whose ID number do you want to update?")
        for index, person in enumerate(people, 1):
            print(f"{index}. {person.name}")
        
        person_choice = input("Enter your choice (number): ")
        try:
            person_choice = int(person_choice)
        except ValueError:
           print("Invalid input. Please enter a number.")
           time.sleep(2)
           continue

        if 1 <= person_choice <= len(people):
           new_idnum = input("Enter the new ID number: ")
           people[person_choice - 1].set_idnum(new_idnum)
           print(f"Updated {people[person_choice - 1].name}'s ID number.")
           print(people[person_choice-1])
        else:
            print("Invalid input. Please select a valid person number.")
            time.sleep(2)
    elif choice == 2:
        print("No IDs updated.")
        break
    else:
        print("Invalid choice. Please choose 1 or 2.")
        time.sleep(2)