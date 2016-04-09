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
        save_items(load_item_list())
        main()
    elif choice == "R" or choice == "r":
        return_item()
        save_items(load_item_list())
        main()
    elif choice == "A" or choice == "a":
        add_item(load_item_list())
        save_items(load_item_list())
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

    # workbook_tuple = tuple(workbook_list)

    # workbook_file.close()

    return workbook_list


def list_all_items(workbook_list):

    print("All items on file (* indicates item out on hire)")

    # Formats the prices to sit in the same position in each row
    counter = 0
    counter_main = 0
    blank_space = ' '
    for i in workbook_list:
        working_list = workbook_list[counter_main]
        spacing_length = 75 - (len(working_list[0] + working_list[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1

        if working_list[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
            counter_main += 1
            blank_space = ' '
        elif working_list[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], "*"))
            counter_main += 1
            blank_space = ' '

        return working_list


def hire_item(workbook_list):
    print("All items available for hire")

    counter = 0
    counter_main = 0
    blank_space = ''
    for i in workbook_list:
        working_list = workbook_list[counter_main]
        spacing_length = 35 - (len(working_list[0] + working_list[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_list)

    while working_list[3] == 'in':
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2]))
        counter_main += 1
        blank_space = ' '
        print(working_list)


def return_item():
    print("Return an item")
#


def add_item(workbook_tuple):
    print("Add an item \n Please enter the details of the new item")

    item_name = input(str("Item name: "))
    item_description = input(str("Description :"))
    item_price = input(str("Price per day: "))

    # item_name = ''.join(item_name)
    # item_description = ''.join(item_description)
    # item_price = ''.join(item_price)

    # new_item_list = []

    new_item_list = [item_name, item_description, item_price]
    # new_item_list = new_item_list.append(new_item_list)

    for row in new_item_list:
        new_item_list. append(row)

    print(new_item_list)

    # new_item_string = []
    # for item in new_item_list:
    #     new_item_string.append(new_item_list)

    # new_item_tuple = tuple(new_item_string)
    #
    # workbook_tuple = (workbook_tuple + new_item_tuple)
    workbook_list = list(workbook_tuple)
    workbook_list = (workbook_list + new_item_list)

    print(workbook_list)

    # workbook_tuple = tuple(workbook_list)

    save_items(workbook_list)

    return workbook_list


def save_items(workbook_list):

    workbook_file = open("items.csv", 'w')
    workbook_writer = csv.writer(workbook_file)

    # workbook_list = list(workbook_tuple)

    # print(workbook_list)

    for row in workbook_list:
        workbook_writer.writerow(row)

    workbook_file.close()


main()



