import re
import sys
import os
import time

file_dict = {}
file_count = {}
def by_space(file):
    startTime = time.time()
    with open(file) as f:
        s = f.read()
    space_counter = 1
    s2 = ''
    prev = ''
    for c in s:
        if c == ' ':
            if prev == '\\':
                s2 = s2 + c
            elif space_counter % 2 == 0:
                space_counter = space_counter + 1
                s2 = s2 + '\n'
            elif space_counter % 2 == 1:
                space_counter = space_counter + 1
                s2 = s2 + c
            else:
                s2 = s2 + c
        else:
            s2 = s2 + c
        prev = c
    endTime = time.time()
    return s2


def by_split(file):

    with open(file) as f:
        s = f.read()
    return re.split(r'(?<!\\)\s', s)


def put_in_dict(my_file, method):
    if method == 'split':
        startTime = time.time()
        result = by_split(my_file)
        for i in range(0, len(result)-1, 2):
            file_dict[result[i]] = result[i+1]
        endTime = time.time()
        print("Метод split выполнился за", endTime - startTime, "секунд")
    else:
        startTime = time.time()
        result = by_space(my_file)
        list_result = result.splitlines()
        for i in list_result:
            a = (i.split(' ', 1))
            file_dict[a[0]] = a[1]
        endTime = time.time()
        print("Метод spaces выполнился за", endTime - startTime, "секунд")
def strip_dict(dictionary):
    for key in dictionary:
        dictionary[key] = dictionary[key].replace('\\', '')


def file_counter(dictionary):
    for key in dictionary:
        file_count[key] = sum([len(files) for r, d, files in os.walk(dictionary[key])])
    sorted_dict= dict(sorted(file_count.items(), key=lambda x: x[1], reverse=True))
    for key in sorted_dict:
        print(key, "имеет", sorted_dict[key], "файлов")

def remove_duplicates(dictionary):
    result = {}
    for key, value in dictionary.items():
        if value not in result.values():
            result[key] = value
    file_dict = result

unsplit_input_file = sys.argv[1]
input_method = sys.argv[2]

if input_method not in ['split', 'spaces']:
    print('Выбранного метода не существет')
    exit(0)
try:
    _ = open(unsplit_input_file, 'r')
except:
    print('Файла или не существует или к нему нет доступа')
    exit(0)

put_in_dict(unsplit_input_file, input_method)
strip_dict(file_dict)
remove_duplicates(file_dict)
file_counter(file_dict)