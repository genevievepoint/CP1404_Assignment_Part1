# Genevieve Point

import csv
# Opens the file in a table format
workbook_file = open('items.csv', 'r')
workbook_list = workbook_file.readlines()

# Separates the rows from each other
counter = 0
for items in workbook_list:
    workbook_list[counter] = items.strip()
    counter += 1

# Separates the items in each row from each other
counter2 = 0
for items in workbook_list:
    workbook_list[counter2] = items.split(',')
    counter2 += 1

# Formats the prices to sit in the same position in each row
counter_main = 0
blank_space = ''
for i in workbook_list:
    working_list = workbook_list[counter_main]
    spacing_length = 38 - (len(working_list[0] + working_list[1]))

    for i in range(1, spacing_length, 1):
        blank_space += ' '
            # counter += 1
    # print(working_list)

    if working_list[3] == 'in':
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
        counter_main += 1
        blank_space = ' '
    elif working_list[3] == 'out':
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
        counter_main += 1
        blank_space = ' '

    # print("{} - {} [{}]{}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], ' ', working_list[2], working_list[3]))
    # counter_main += 1
    # blank_string = ' '



def menu():
    print("Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit")
    choice = input()

    if choice == "L" or choice == "l":
        list_all_items()
        menu()
    elif choice == "H" or choice == "h":
        print("Hire item")
        menu()
    elif choice == "R" or choice == "r":
        print("Return an item")
        menu()
    elif choice == "A" or choice == "a":
        add_item()
        menu()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("Please enter a valid choice")
        menu()


menu()


def list_all_items():

    workbook_file = open('items.csv', 'r')
    # workbook_reader = csv.reader(workbook_file)
    workbook_list = workbook_file.readlines()

    counter = 0
    for items in workbook_list:
        workbook_list[counter] = items.strip()
        counter += 1

    counter2 = 0
    for items in workbook_list:
        workbook_list[counter2] = items.split(',')
        counter2 += 1


    counter_main = 0
    blank_space = ''
    for i in workbook_list:
        working_list = workbook_list[counter_main]
        spacing_length = 38 - (len(working_list[0] + working_list[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            # counter += 1
            # print(working_list)


        if working_list[3] == 'in':
            return("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
            # counter_main += 1
            # blank_space = ' '
        elif working_list[3] == 'out':
            return("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
            # counter_main += 1
            # blank_space = ' '
    # print("{} - {} [{}]{}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], ' ', working_list[2], working_list[3]))
    # counter_main += 1
    # blank_string = ' '

    workbook_file.close()

    # list_items()


def hire_item(working_list, blank_space, counter_main):

    working_list[3] == 'in'
    print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
    counter_main += 1
    blank_space = ' '


def add_item():
    for row in workbook_list:
        workbook_list.append(row)

        workbook_list[0] = input("Item name: ")
        workbook_list[1] = input("Description: ")
        workbook_list[2] = input("Price per day: ")






workbook_file.close()

















