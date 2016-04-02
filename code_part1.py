import csv

print("Items for Hire - By Genevieve Point")


def menu():
    print("Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit \n")
    choice = input()

    if choice == "L" or choice == "l":
        load_items()
    elif choice == "H" or choice =="h":
        hire_item()
    elif choice == "R" or choice == "r":
        return_item()
    elif choice == "A" or choice == "a":
        add_item()
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
        row = row.strip().splot(',')
        row_info = row[0], row[1], row[2], row[3]
        if row_info == "out":
            print("*")
        else:
            print(" ")
        print(row)

    workbook_file.close()


def hire_item():

    # allows user to hire an item from items file
    workbook_file = open('items.csv', 'r')
    workbook_reader = csv.reader(workbook_file)
    for row in workbook_reader:

        print(row)

    workbook_file.close()
    # for line in lines:
    # if country_name in line:
    #     line = line.strip().split(',')
    #     line_info = line[0], line[1], line[2]
    #     return tuple(line_info)


def return_item():

    # allows user to return an item
    workbook_file = open('items.csv', 'r')
    workbook_reader = csv.reader(workbook_file)
    for row in workbook_reader:
        print(row)

    workbook_file.close()



def add_item():

    # allows user to add an item to the list
    workbook_file = open('items.csv', 'w')
    workbook_writer = csv.writer(workbook_file)
    for row in workbook_writer.append():
         row = input("Please enter a new item")



    workbook_file.close()