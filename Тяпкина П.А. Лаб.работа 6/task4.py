import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file):
    with open(file, 'r') as input_:
        list_ = input_.readlines()
        headers_list = list_[0][:-1].split(',')
        data_list = [line[:-1] for line in list_[1:]]

        data_full = []          #список, элементы которого - это списки элементов строк
        index = 0
        for line in data_list:
            line = data_list[index].split(',')
            data_full.append(line)
            index = index + 1

        list_dict = []          #список словарей формируется ссылками на список заголовков и списки данных
        index_out = 0           #внешний медленный индекс, перебирающий строки данных в таблице
        for line in data_full:
            index_in = 0        #внутренний быстрый индекс, ставящий в соответствие столбцы данных и заголовки
            dict_ = {}
            for row in headers_list:
                dict_[headers_list[index_in]] = data_full[index_out][index_in]
                index_in = index_in + 1
            list_dict.append(dict_)
            index_out = index_out + 1
        return list_dict

'''        line1 = data_list[0].split(',')
        line2 = data_list[1].split(',')
        line3 = data_list[2].split(',')
        line4 = data_list[3].split(',')

        index = 0
        dict_1 = {}
        for row in headers_list:
            dict_1[headers_list[index]] = line1[index]
            index = index + 1
        dict_2 = {}
        index = 0
        for row in headers_list:
            dict_2[headers_list[index]] = line2[index]
            index = index + 1
        list_dict = [dict_1, dict_2]
'''

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
#
