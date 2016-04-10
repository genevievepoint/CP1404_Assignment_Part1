# Genevieve Point
# 11 April 2016
# https://github.com/genevievepoint/CP1404_Assignment_Part1
#
import csv

MENU = "\n Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit"


def main():
    print("Items for Hire - By Genevieve Point")
    load_item_list()

    item_list = load_item_list()
    # print(item_list)

    # choice = input()
    print(MENU)
    print()
    chosenMenuOption = input('Input your selection: ')
    while chosenMenuOption != 'Q' or chosenMenuOption != 'q':
        if chosenMenuOption == 'L' or chosenMenuOption == 'l':
            list_all_items(item_list)
            # save_items(item_list)
        elif chosenMenuOption == 'H'or chosenMenuOption == 'h':
            hire_item(item_list)
            # save_items(item_list)
        elif chosenMenuOption == 'R' or chosenMenuOption == 'r':
            return_item(item_list)
            # save_items(item_list)
        elif chosenMenuOption == 'A' or chosenMenuOption == 'a':
            item_list = add_item(item_list)
            print(item_list)
            # save_items(item_list)
        else:
            print("Please enter a valid choice")

        print(MENU)
        print()
        chosenMenuOption = input('Input your selection: ')
    save_items(item_list)
    return quit()


# def load_items_list:
#     open csv
#     read csv
#     count = 0
#     for item in item_list:
#         items.strip()
#         count += 1

#     count2 = 0
#     for item in item_list:
#         items.split(',')
#         count2 += 1

#     close workbook file
#     return item_list


def load_item_list():
    # Opens the file in a table format
    workbook_file = open('items.csv', 'r')
    item_list = workbook_file.readlines()

    # Separates the rows from each other
    counter = 0
    for items in item_list:
        item_list[counter] = items.strip()
        counter += 1

    # Separates the items in each row from each other
    counter2 = 0
    for items in item_list:
        item_list[counter2] = items.split(',')
        counter2 += 1

    workbook_file.close()

    return item_list


def list_all_items(item_list):
    print(item_list)
    print("All items on file (* indicates item out on hire)")

    # Formats the prices to sit in the same position in each row
    counter = 0
    main_counter = 0
    blank_space = ' '
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 45 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1

        if working_items[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2], " "))
            main_counter += 1
            blank_space = ' '
        elif working_items[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2], " * "))
            main_counter += 1
            blank_space = ' '

    return item_list


# def hire_item(item_list):
#     print sub-menu name

#     count = 0
#     main_count = 0
#     blank_space = ' '
#     for i in item_list:
#         working_item = item_list[main_counter
#         spacing_length = total length - length of working_items[0] and workin_items[1]

#         for i in range(1, spacing_length, 1):
#             blank_space += ' '
#             count += 1

#         if working_items[3] == 'in'
#             print formatted string
#             blank_space += ' '
#             main_count += 1

#         users_choice = int(input(prompt))
#         hire_select = item_list[users_choice]
#         hire_select[3] = 'out'
#         item_list[users_choice] = hire_select

#         return item_list

def hire_item(item_list):
    print("All items available for hire")

    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 45 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        print(working_items)

        for i in working_items:
            if working_items[3] == 'in':
                print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
                blank_space = ' '
                main_counter += 1
                # print(working_items)

            else:
                print("no items available for hire")

        users_choice = input("Please enter an item number: ")
        if users_choice != int:
            users_choice = int(input("Please enter an item number: "))
        hire_select = item_list[users_choice]
        hire_select[3] = "out"
        item_list[users_choice] = hire_select

        print(users_choice, working_items[0], "has been hired for", working_items[2])

        return item_list


def return_item(item_list):
    print("Return an item")

    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 45 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_items)

        if working_items[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
            main_counter += 1
            blank_space = ' '
            print(working_items)

        else:
            print("No items are hired")

        users_choice = input("Please enter an item number: ")
        if users_choice != int:
            users_choice = int(input("Please enter an item number: "))
        hire_select = item_list[users_choice]
        hire_select[3] = "in"
        item_list[users_choice] = hire_select

        print(hire_select, working_items[0], "has been returned")
        return item_list


def add_item(item_list):

    print("Add an item \n Please enter the details of the new item")

    # Asks the user to input the information about the new item
    item_name = input(str("Item name: "))
    while item_name == '':
        item_name = input("Item name: ")
    item_description = input(str("Description: "))
    while item_description == '':
        item_description = input("Description: ")
    item_price = input("Price per day: ")
    while item_price == ' ' and item_price == str:
        item_price = input("Price per day: ")

    # Sets the items availability to in automatically
    item_availability = "in"

    # Stores the data as a list
    new_item_list = [item_name, item_description, item_price, item_availability]
    print(new_item_list)

    # Adds the new item list to the end of the existing items
    item_list.append(new_item_list)

    return item_list


def save_items(item_list):

    workbook_file = open("items.csv", 'w')
    workbook_writer = csv.writer(workbook_file)

    # Overwrite all data in file with item list and any changes made
    for items in item_list:
        workbook_writer.writerow(items)

    workbook_file.close()


main()
