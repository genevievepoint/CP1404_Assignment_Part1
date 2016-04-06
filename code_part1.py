# Genevieve Point
import csv


def load_item_list():
    # Opens the file in a table format
    workbook_file = open('items.csv', 'r')
    workbook_list = workbook_file.readlines()

    # working_list = []
    #
    # for row in workbook_list:
    #     working_list.append(row)

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
        spacing_length = 35 - (len(working_list[0] + working_list[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1
        # print(working_list)

        if working_list[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
            counter_main += 1
            blank_space = ' '
        elif working_list[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
            counter_main += 1
            blank_space = ' '

    workbook_file.close()


# def menu():
#     print("Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit")
#     choice = input()
#
#     if choice == "L" or choice == "l":
#         return list_all_items()
#         menu()
#     elif choice == "H" or choice == "h":
#         return hire_item()
#         menu()
#     elif choice == "R" or choice == "r":
#         return return_item()
#         menu()
#     elif choice == "A" or choice == "a":
#         return add_item()
#         menu()
#     elif choice == "Q" or choice == "q":
#         return quit()
#     else:
#         print("Please enter a valid choice")
#         menu()
#
#
# menu()
#
#
# def list_all_items(working_list, counter_main, blank_space):
#     if working_list[3] == 'in':
#         print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
#         # counter_main += 1
#         # blank_space = ' '
#     elif working_list[3] == 'out':
#         print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
#         # counter_main += 1
#         # blank_space = ' '
#     # print("{} - {} [{}]{}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], ' ', working_list[2], working_list[3]))
#     # counter_main += 1
#     # blank_string = ' '
#
#
#     # list_items()
#
#
# def hire_item(working_list, blank_space, counter_main):
#
#     working_list[3] == 'in'
#     print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
#     counter_main += 1
#     blank_space = ' '
#
# def return_item():
#     print("Return an item")
#
# def add_item():
#     for row in workbook_list:
#         workbook_list.append(row)
#
#         workbook_list[0] = input("Item name: ")
#         workbook_list[1] = input("Description: ")
#         workbook_list[2] = input("Price per day: ")
#
#
# def main():
#     load_items
#     menu()

print(load_item_list())