import csv

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
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2], " "))
        counter_main += 1
        blank_space = ' '
    elif working_list[3] == 'out':
        print("{} - {} ({}){}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], blank_space, working_list[2],"*"))
        counter_main += 1
        blank_space = ' '
    #
    # print("{} - {} [{}]{}\t\t\t= ${}\t{}".format(counter_main, working_list[0], working_list[1], ' ', working_list[2], working_list[3]))
    # counter_main += 1
    # blank_string = ' '

# print(workbook_list)


# print(workbook_list)

workbook_file.close()