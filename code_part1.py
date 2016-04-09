# Genevieve Point
import csv

MENU = "\n Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit"


def main():
    print("Items for Hire - By Genevieve Point")
    load_item_list()
    # print(load_item_list())
    print(MENU)

    item_list = load_item_list()
    # print(item_list)

    # choice = input()
    print(MENU)
    print()
    chosenMenuOption = input('Input your selection: ')
    while chosenMenuOption != 'Q' or chosenMenuOption != 'q':
        if chosenMenuOption == 'L' or chosenMenuOption == 'l':
            list_all_items(item_list)
        elif chosenMenuOption == 'H'or chosenMenuOption == 'h':
            hire_item(item_list)
        elif chosenMenuOption == 'R' or chosenMenuOption == 'r':
            return_item(item_list)
        elif chosenMenuOption == 'A' or chosenMenuOption == 'a':
            add_item(item_list)
        else:
            print("Please enter a valid choice")
            print(MENU)
            print()
        chosenMenuOption = input('Input your selection: ')
    return quit()


    # if choice == "L" or choice == "l":
    #     list_all_items(item_list)
    #     main()
    # elif choice == "H" or choice == "h":
    #     hire_item(item_list)
    #     save_items(item_list)
    #     main()
    # elif choice == "R" or choice == "r":
    #     return_item(item_list)
    #     save_items(item_list)
    #     main()
    # elif choice == "A" or choice == "a":
    #     add_item(item_list)
    #     save_items(item_list)
    #     main()
    # elif choice == "Q" or choice == "q":
    #     return quit()
    # else:
    #     print("Please enter a valid choice")


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

    # workbook_file.close()

    return item_list


def list_all_items(item_list):

    print("All items on file (* indicates item out on hire)")

    # Formats the prices to sit in the same position in each row
    counter = 0
    main_counter = 0
    blank_space = ' '
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 35 - (len(working_items[0] + working_items[1]))

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


def hire_item(item_list):
    print("All items available for hire")

    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 35 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_items)

        if working_items[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
            main_counter += 1
            blank_space = ' '
            print(working_items)

    hiring_item = input("Enter an item number: ")

    return item_list

def return_item(item_list):
    print("Return an item")

    counter = 0
    main_counter = 0
    blank_space = ''
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 35 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_items)

        if working_items[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2]))
            main_counter += 1
            blank_space = ' '
            # print(working_items)

    return item_list


def add_item(item_list):
    print("Add an item \n Please enter the details of the new item")

    item_name = input(str("Item name: "))
    while item_name == ' ':
        item_name = input("Item name: ")

    item_description = input(str("Description: "))
    while item_description == ' ':
        item_description = input("Description: ")

    item_price = input("Price per day: ")
    while item_price == ' ':
        item_price = input("Price per day: ")

    # item_name = ''.join(item_name)
    # item_description = ''.join(item_description)
    # item_price = ''.join(item_price)

    new_item_list = []


    # .append for each
    for item_name in new_item_list:
        new_item_list.append(item_name)
        for item_description in new_item_list:
            new_item_list.append(item_description)
            for item_price in new_item_list:
                new_item_list.append(item_price)
    # new_item_list = [item_name, item_description, item_price]
    # new_item_list = new_item_list.append(new_item_list)

    for new_item_list in item_list:
        item_list. append(new_item_list)

    print(new_item_list)

    # new_item_string = []
    # for item in new_item_list:
    #     new_item_string.append(new_item_list)

    item_list.append(new_item_list)
    # .append again
    print(item_list)

    # workbook_tuple = tuple(workbook_list)

    # save_items(workbook_list)

    return item_list


def save_items(item_list):

    workbook_file = open("items.csv", 'w')
    workbook_writer = csv.writer(workbook_file)

    # workbook_list = list(workbook_tuple)

    # print(workbook_list)

    for row in item_list:
        workbook_writer.writerow(row)

    workbook_file.close()


main()



