import csv

print("Items for Hire - By Genevieve Point")


def menu():
    print("Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit \n")
    choice = input()

    if choice == "L" or choice == "l":
        print("load_items()")
    elif choice == "H" or choice =="h":
        print("hire_item()")
    elif choice == "R" or choice == "r":
        print("load_items()")
    elif choice == "A" or choice == "a":
        print("load_items()")
    elif choice == "Q" or choice == "q":
        print("quit()")
    else:
        print("Please enter a valid choice")
        menu()

menu()




def load_items():

# reads items file
    workbook_file = open('items.csv', 'r')
    workbook_reader = csv.reader(workbook_file)
    for row in workbook_reader:
        print(row)

    workbook_file.close()


def hire_item():

# reads items file
    workbook_file = open('items.csv', 'r')
    workbook_reader = csv.reader(workbook_file)
    for row in workbook_reader:
        print(row)

    workbook_file.close()


