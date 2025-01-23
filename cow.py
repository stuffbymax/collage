import time

while True:
  print("Choose an action:")
  print("1. moo")
  print("2. exit")

  choice = input("Enter your choice: ")
  if not choice.isdigit():
    print("Invalid input. Please enter a number.")
    time.sleep(2)
    continue  # Go back to the start of the loop

  choice = int(choice)

  if choice == 1:
    print("_______________________")
    print("< Have you mooed today? >")
    print("-----------------------")
    print("       \   ^__^")
    print("        \  (oo)\_______")
    print("           (__)\       )\\/\\")
    print("              ||----w |")
    print("              ||     ||")
  elif choice == 2:
    print("Exiting...")
    break  # Exit the while loop, ending the program
  else:
    print("Invalid choice. Please enter 1 or 2.")
    time.sleep(2) # give time to see error
