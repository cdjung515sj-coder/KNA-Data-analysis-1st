# 실습 6. 폴더에 csv 하일만 골라내기

import os

file_list = os.listdir("data")

csv_file_empty = []

for file_name in file_list:
    if file_name.endswith(".csv"):
        file_path = os.path.join(os.getcwd(),file_name)
        csv_file_empty.append(file_path)

print("[CSV]목록 ")
for path in csv_file_empty:
    print(path)