# 실습 3. os 폴더 목록 살펴보기

import os

current_path = os.getcwd()
file_list = os.listdir(current_path)

for file_name in file_list:
    print(file_name)

for file_name in file_list:
    if file_name.endswith(".csv"):  
        print(file_name)