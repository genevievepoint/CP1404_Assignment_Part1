# Genevieve Point

class ItemList:
    def item_list(self):
        counter = 1
        for i in list_of_item_class_objects:
            current_item = list_of_item_class_objects[counter]
            spacing_length = 40 - (len(current_item[0] + current_item[1]))

            for i in range(1, spacing_length, 1):
                blank_string += ' '


            if current_item.status == 'in':
                print("{} - {} ({}){}\t\t\t= ${:.2f}".format(counter, current_item.name, current_item.description,
                                                             blank_string, float(current_item.price)))

            elif current_item.status == 'out':
                print("{} - {} ({}){}\t\t\t= ${:.2f}{}".format(counter, current_item.name, current_item.description,
                                                               blank_string, float(current_item.price), '*'))

            counter += 1
            blank_string = ' '
