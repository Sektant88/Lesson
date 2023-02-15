from класс import Person

person = Person()

while True:

    print("1. Enter new data")
    print("2. Search by name")
    print("3. Calculate age")
    print("4. Save to file")
    print("5. Load from file")
    print("0. Exit")


    choice = int(input("Enter choice: "))


    if choice == 1:
        person.enter_data()
    elif choice == 2:
        person.search()
    elif choice == 3:
        person.calculate_age()
    elif choice == 4:
        person.save_to_file()
    elif choice == 5:
        person.load_from_file()
    elif choice == 0:
        break
    else:
        print("Invalid choice")