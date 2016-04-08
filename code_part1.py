# Genevieve Point
import csv

MENU = "\n Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit"


def main():
    print("Items for Hire - By Genevieve Point")
    load_item_list()
    # print(load_item_list())
    print(MENU)

    choice = input()

    if choice == "L" or choice == "l":
        list_all_items(load_item_list())
        main()
    elif choice == "H" or choice == "h":
        hire_item(load_item_list())
        main()
    elif choice == "R" or choice == "r":
        return_item()
        main()
    elif choice == "A" or choice == "a":
        add_item()
        main()
    elif choice == "Q" or choice == "q":
        return quit()
    else:
        print("Please enter a valid choice")
        main()


def load_item_list():
    # Opens the file in a table format
    workbook_file = open('items.csv', 'r')
    workbook_list = workbook_file.readlines()

    # workbook_items = []
    #
    # for row in workbook_reader:
    #     workbook_items.append(row)


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

    workbook_tuple = tuple(workbook_list)

    # # Formats the prices to sit in the same position in each row
    # counter_main = 0
    # blank_space = ''
    # for i in workbook_list:
    #     working_list = workbook_list[counter_main]
    #     spacing_length = 35 - (len(working_list[0] + working_list[1]))
    #
    #     for i in range(1, spacing_length, 1):
    #         blank_space += ' '
    #         counter += 1
    #     # print(working_list)
    #
    #     if working_list[3] == 'in':
    #         print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
    #         counter_main += 1
    #         blank_space = ' '
    #     elif working_list[3] == 'out':
    #         print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
    #         counter_main += 1
    #         blank_space = ' '

    workbook_file.close()

    return workbook_tuple


def list_all_items(workbook_tuple):

    # Formats the prices to sit in the same position in each row
    counter = 0
    counter_main = 0
    blank_space = ''
    for i in workbook_tuple:
        working_tuple = workbook_tuple[counter_main]
        spacing_length = 35 - (len(working_tuple[0] + working_tuple[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_list)

        if working_tuple[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_tuple[0], working_tuple[1], blank_space, working_tuple[2], " "))
            counter_main += 1
            blank_space = ' '
        elif working_tuple[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_tuple[0], working_tuple[1], blank_space, working_tuple[2],"*"))
            counter_main += 1
            blank_space = ' '

    return counter_main, blank_space


def hire_item(working_tuple):
    print("All items available to hire")
    counter_main = 0
    blank_space = ' '

    if working_tuple[3] == 'in':
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_tuple[0], working_tuple[1], blank_space, working_tuple[2]))
        counter_main += 1
        # blank_space = ' '
        print(working_tuple)

def return_item():
    print("Return an item")
#


def add_item():
    print("Add an item")

    # for row in working_list:
    #     workbook_list.extend(row)
    #
    #     workbook_list[0] = input("Item name: ")
    #     workbook_list[1] = input("Description: ")
    #     workbook_list[2] = input("Price per day: ")


main()



