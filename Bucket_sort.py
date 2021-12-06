import json
import yaml
from typing import List


def insertion_sort(bucket: list,  parametr: int):
    #a = bucket[0]
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        a = bucket[j]
        #a = bucket[j]
        while (j >= 0 and var.get(parametr) < a.get(parametr)):
            bucket[j + 1] = bucket[j]
            j = j - 1
            bucket[j + 1] = var
    return bucket


class Bucket_Sort:
    """класс для работы с файлом и сортировки данных"""

    def __init__(self) -> None:
        pass

    def read_json_txt(self, filename):
        with open(filename, "r") as f:
            tmp = json.load(f)
            return tmp

    def write_json_txt(self, filename, collection: list) -> None:
        with open(filename, 'w') as f:
            json.dump(collection, f, default_flow_style=False)

    def read_yaml(self, filename):
        with open(filename, "r") as f:
            return yaml.safe_load(f)

    def write_yaml(self, filename, collection: list) -> None:
        with open(filename, "w") as f:
            yaml.dump(collection, f, default_flow_style=False)

    def print_collection(cls, list: list, count):
        for i in range(count):
            for key, value in list[i].items():
                print('{:15s}'.format(key), ':', value)
            print("_________________________________________")

    def bucket_sort(self, input_list: list, parameter: int):
        i = 0
        max = input_list[i]
        while i < len(input_list):
            a = input_list[i]
            if a.get(parameter) > max.get(parameter):
                max = input_list[i]
            i += 1
        size = max.get(parameter) / len(input_list)

        buckets_list = []
        for x in range(51528):
            buckets_list.append([])

        k = 0
        a = input_list[k]

        for k in range(len(input_list)):
            a = input_list[k]
            j = int(a.get(parameter) / size)
            if j != len(input_list):
                buckets_list[j].append(input_list[k])
            else:
                buckets_list[len(input_list) - 1].append(input_list[k])

        for z in range(len(input_list)):
            insertion_sort(buckets_list[z], parameter)

        final_output = []
        for x in range(len(input_list)):
            final_output = final_output + buckets_list[x]
        return final_output





