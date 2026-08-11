# 실습 3. 여러 파일 묶어 처리하기
# 다음과 같은 식의 리스트를 만들어 반복문으로 처리해보자
# for 문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도

file_names = ["08_press_over90.csv", "08_press.csv", "result.csv"]

success = 0

for name in file_names:
    try:
        with open(name,"r,")
    except: