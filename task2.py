# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, splitter=","):
    set_1 = set(str_1.split(splitter))
    result = set_1.intersection(str_2.split(splitter))
    general_list = sorted(list(result))

    return general_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
