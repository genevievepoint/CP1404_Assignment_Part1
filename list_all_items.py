def list_all_items(item_list):

    print(item_list)
    print("All items on file (* indicates item out on hire)")

    # Formats the prices to sit in the same position in each row
    counter = 0
    main_counter = 0
    blank_space = ' '
    for i in item_list:
        working_items = item_list[main_counter]
        spacing_length = 55 - (len(working_items[0] + working_items[1]))

        for i in range(1, spacing_length, 1):
            blank_space += ' '
            counter += 1

        if working_items[3] == 'in':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2], " "))
            blank_space = ' '
            main_counter += 1
        elif working_items[3] == 'out':
            print("{} - {} ({}){}\t\t\t= ${}\t{}".format(main_counter, working_items[0], working_items[1], blank_space, working_items[2], " * "))
            blank_space = ' '
            main_counter += 1

    return item_list