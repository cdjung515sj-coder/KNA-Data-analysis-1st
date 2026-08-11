# 실습 4. os로 파일 존재 확인하기

import os
print(os.getcwd())
path = os.path.join("data", "08_press.csv")
is_exist = os.path.exists(path)
print(f"경로가 있는는가? : {is_exist}")

if is_exist:
    print(f"파일 있음 : {path}")
else:
    print(f"파일 없음 : {path}")
