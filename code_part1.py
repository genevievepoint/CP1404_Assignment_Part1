# Genevieve Point#
import csv

# menu()
print("Items for Hire - By Genevieve Point")# 06/04/2016


workbook_file = open('items.csv', 'r')
workbook_reader = csv.reader(workbook_file)

items_list = []

for row in workbook_reader:
    # row = row.split()
    # row_info = row.strip('\n')
    # items_list.append(row)
    items_list = row
    # print(items_list)

counter_strip = 0
for list in items_list:
    items_list[counter_strip] = items_list[counter_strip].strip()
    counter_strip += 1

counter_split = 0
for item in items_list:
    items_list[counter_split] = items_list[counter_split].split(',')
    counter_split += 1


counter_main = 0
for i in items_list:
    working_list = items_list[counter_main]

    print("$()".format(counter_main, working_list[0], working_list[1], working_list[2]))

workbook_file.close()


def menu():
    print("Menu: \n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd an item \n (Q)uit \n")
    choice = input()

    if choice == "L" or choice == "l":
        list_items(items_list)
        menu()
    elif choice == "H" or choice == "h":
        hire_item()
        menu()
    elif choice == "R" or choice == "r":
        return_item()
        menu()
    elif choice == "A" or choice == "a":
        add_item()
        menu()
    elif choice == "Q" or choice == "q":
        print("quit()")
    else:
        print("Please enter a valid choice")
        menu()
    def load_items():
        print("List all items")




# menu()

def list_items(items_list):
    print("All items on file")
    if items_list == "out":
        print("*")


def hire_item():
    print("Hire an item")
    # for line in lines:
    # if country_name in line:
    #     line = line.strip().split(',')
    #     line_info = line[0], line[1], line[2]
    #     return tuple(line_info)

# menu()


def return_item():
    print("Return an item")


# menu()


def add_item():
    print("Add an item for hire")


# menu()