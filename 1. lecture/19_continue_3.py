# 반복문 안에서 예외처리

my_list = ["123", "456", "32", "53"]

for text in my_list:
    print(text)


print("---")
# 변환해보자

for text in my_list:
    my_number = int(text)
    print(my_number)


print("---")
# 문제를 넣어보자
# my_list = ["123", "456", "늙크크", "32", "53"]

# for text in my_list:
#     my_number = int(text)
#     print(my_number)  # ValueError: invalid literal for int() with base 10: '늙크크'


print("---")
# 문제 해결
my_list = ["123", "456", "늙크크", "32", "53"]

for text in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고
    # 계속 반복을 이어서 진행시키기

    try:
        my_number = int(text)
        print(my_number)
    except:
        print("문제발생")


print("---")
for text in my_list:

    try:
        my_number = int(text)
    except:
        print("문제발생")
        # 문제가 생겼다면 더 이상 반복문 안의 출력까지 이어가면 안되겠다
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

        # continue를 넣는다면?
        continue

    print(my_number)
    # 123
    # 456
    # 문제발생
    # 456
    # 32
    # 53

print("---")
for text in my_list:

    try:
        my_number = int(text)
    except:
        print("문제발생")
        # continue를 넣는다면?
        continue

    print(my_number)


print("--------------------------")
my_list = ["123", "456", "늙크크", "32", "53"]

problems = 0

for text in my_list:

    try:
        my_number = int(text)
    except:
        # 갈 때 가더라도 문제상황 카운팅 정도는 괜찮자나~
        problems += 1
        continue

    print(my_number)

print(f"{problems}개는 문제가 있어서 건너뜀")
