import random
import time
import json

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

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.Idnum}"

    def to_dict(self): # added to assist in saving
        return {
            "age": self.age,
            "name": self.name,
            "Idnum": self.Idnum
        }

    @classmethod
    def from_dict(cls, data): # added to assist in loading
        return cls(data["age"], data["name"], data["Idnum"])

def save_people(people, filename):
    """Saves the list of people to a JSON file."""
    people_data = [person.to_dict() for person in people]
    with open(filename, "w") as file:
        json.dump(people_data, file, indent=4) # added indent=4 for human readability

def load_people(filename):
    """Loads a list of people from a JSON file."""
    try:
        with open(filename, "r") as file:
            people_data = json.load(file)
        return [Person.from_dict(data) for data in people_data]
    except FileNotFoundError:
        return [] #Return an empty list if no save file

# Default list
people = [
    Person(31, "Ben", "123456"),
    Person(42, "Paul", "987654"),
    Person(22, "Sarah", "456789"),
    Person(60, "John", "789012")
]

# Load people data if it exists
filename = "people_data.json"
people = load_people(filename)

# Initial print
for person in people:
    print(person)

while True:
    print("\nWhat do you want to do?")
    print("1. Update ID numbers")
    print("2. Save")
    print("3. Quit")

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
        save_people(people, filename)
        print(f"Saved people data to {filename}.")
        time.sleep(2)

    elif choice == 3:
        print("Quitting.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        time.sleep(2)