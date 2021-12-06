from typing import List

from Bucket_sort import Bucket_Sort

filename_txt = "res.txt"
filename_yaml = "res.yaml"
file = Bucket_Sort()
data = file.read_json_txt(filename_txt)
parameters: list[str] = ["age", "passport_number"]
data = file.bucket_sort(data, parameters[0])
file.write_yaml(filename_yaml, data)
tmp = file.read_yaml(filename_yaml)
file.print_collection(tmp, 10)
