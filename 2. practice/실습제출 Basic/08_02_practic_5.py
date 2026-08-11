# 실습 5. datetime으로 점검 기록 남기기

import os
from datetime import datetime

folder_file_list = os.listdir()
folder_file_count = len(folder_file_list)

now = datetime.now()

print(f"파일 {folder_file_count}개 , 점검 시각 : {now}")
