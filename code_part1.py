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
        print(MENU)
    elif choice == "H" or choice == "h":
        hire_item(workbook_items)
        print(MENU)
    elif choice == "R" or choice == "r":
        return_item()
        print(MENU)
    elif choice == "A" or choice == "a":
        add_item()
        print(MENU)
    elif choice == "Q" or choice == "q":
        return quit()
    else:
        print("Please enter a valid choice")
        print(MENU)


def load_item_list():
    # Opens the file in a table format
    workbook_file = open('items.csv', 'r')
    workbook_reader = csv.reader(workbook_file)

    workbook_items = []

    for row in workbook_reader:
        workbook_items.extend(row)


            # Separates the rows from each other
    counter = 0
    for items in workbook_items:
        workbook_items[counter] = items.strip()
        counter += 1

    # Separates the items in each row from each other
    counter2 = 0
    for items in workbook_items:
        workbook_items[counter2] = items.split(',')
        counter2 += 1

    # Formats the prices to sit in the same position in each row
    counter_main = 0
    blank_space = ''
    for i in workbook_items:
        working_list = workbook_items[counter_main]
        spacing_length = 35 - (len(working_list[0] + working_list[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_list)

    workbook_file.close()

    return workbook_items


def list_all_items(workbook_items):

        if working_list[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
            counter_main += 1
            blank_space = ' '
        elif working_list[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
            counter_main += 1
            blank_space = ' '

        return(working_list)


def hire_item(working_list, counter_main, blank_space):

    # working_list[3] == 'in'
    # print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2]))
    # counter_main += 1
    blank_space = ' '
    print(working_list)

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



