# Genevieve Point
# 11 April 2016
# https://github.com/genevievepoint/CP1404_Assignment_Part1
# This program is a lending and returning service that allows users to hire and return items as well as add in new items
#     it tells the user what items are stored, and whether they are available or not. All items are automatically saved
#     when the user quits.


import csv

MENU = "\n Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit"


def main():
    print("Items for Hire - By Genevieve Point")
    load_item_list()

    item_list = load_item_list()

    print(MENU)
    print()
    chosen_menu_option = input('Input your selection: ')
    while chosen_menu_option != 'Q' or chosen_menu_option != 'q':
        if chosen_menu_option == 'L' or chosen_menu_option == 'l':
            list_all_items(item_list)
        elif chosen_menu_option == 'H'or chosen_menu_option == 'h':
            hire_item(item_list)
        elif chosen_menu_option == 'R' or chosen_menu_option == 'r':
            return_item(item_list)
        elif chosen_menu_option == 'A' or chosen_menu_option == 'a':
            item_list = add_item(item_list)
            print(item_list)
        else:
            print("Please enter a valid choice")

        print(MENU)
        print()
        chosen_menu_option = input('Input your selection: ')
    save_items(item_list)
    quit()
    print("Have a nice day!")


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
#
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

#         if working_items[3] == 'in':
#             print formatted string
#             blank_space += ' '
#             main_count += 1
#         elif working_items[3] == 'out':
#             pass
#         else:
#             print no items message
#         users_choice = int(input(prompt))
#         hire_select = item_list[users_choice]
#         hire_select[3] = 'out'
#         item_list[users_choice] = hire_select

#         return item_list

def hire_item(item_list):
    print("All items that are available for hire")

    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 45 - (len(working_items[0] + working_items[1]))

        for item in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1

        if working_items[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
            blank_space = ' '
            main_counter += 1

            # Asks the user what item they would like to hire and checks it out
            users_choice = input("Please enter an item number: ")
            if users_choice != int:
                users_choice = int(input("Please enter an item number: "))
            hire_select = item_list[users_choice]
            hire_select[3] = "out"
            item_list[users_choice] = hire_select

            print(users_choice, working_items[0], "has been hired for", working_items[2])

        elif working_items[3] == 'out':
            pass

    else:
        print("No items available for hire")


        return item_list


def return_item(item_list):
    print("Items able to be returned")

    # Formats the content for the user
    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 45 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1

        if working_items[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
            main_counter += 1
            blank_space = ' '

            users_choice = input("Please enter an item number: ")
            if users_choice != int:
                users_choice = int(input("Please enter an item number: "))
            hire_select = item_list[users_choice]
            hire_select[3] = "in"
            item_list[users_choice] = hire_select

            print(hire_select, working_items[0], "has been returned")

        elif working_items[3] == 'in':
            pass

    else:
        print("No items are hired")

        return item_list


def add_item(item_list):

    print("Add an item \n Please enter the details of the new item")

    # Asks the user to input the information about the new item
    item_name = input(str("Item name: "))
    while item_name == '':
        print("Item name cannot be blank")
        item_name = input("Item name: ")
    item_description = input(str("Description: "))
    while item_description == '':
        print("Item Description cannot be blank")
        item_description = input("Description: ")
    item_price = input("Price per day: ")
    while item_price == '' and item_price == str:
        print("Item price must be a number and cannot be blank")
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
