import timeit
from typing import List
from Bucket_sort import Bucket_Sort

filename_txt = "res.txt"
filename_yaml = "res.yaml"
statistics = open("statistics.txt", 'w')
file = Bucket_Sort()
data = file.read_json_txt(filename_txt)
parameters: list[str] = ["age", "passport_number"]
start_time = timeit.default_timer()
data = file.bucket_sort(data, parameters[0])
print("Время сортировки: ")
print(timeit.default_timer() - start_time)
statistics.write('Время сортировки: ')
statistics.write(str(timeit.default_timer() - start_time))
start_time = timeit.default_timer()
file.write_yaml(filename_yaml, data)
print("\nВремя сериализации: ")
print(timeit.default_timer() - start_time)
statistics.write('\nВремя сериализации: ')
statistics.write(str(timeit.default_timer() - start_time))
tmp = file.read_yaml(filename_yaml)
file.print_collection(tmp, 10)
