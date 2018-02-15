def print_menu():
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete and entry')
    print('4. List all entries')
    print('5. Quit')
    print()

numbers = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("What do you want to do (1-5): "))
    if menu_choice == 1:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice != 5:
        print_menu()