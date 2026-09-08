# 실습 2. 견고한 예외처리
# 반복문에서 불량 줄 건너뛰기
# 소숫점 이하의 숫자가 포함된 숫자들을 20개 정도 만들어 문자로 리스트 배열에 담아주세요 "123.45"
# 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시켜 주세요 "영크크"
# 위 리스트 데이터를 사용해서 문제를 풀어주세요.

list = [
    "파이팅",
    "13.2",
    "134.24",
    "32.33",
    "2345.23",
    "32.11",
    "영크크",
    "235.03",
    "2391.842",
    "333.33",
    "2019.36",
    "515.00",
    "313.95",
    "침대",
    "192",
    "38.98",
    "잠",
    "휴식",
    "3392.10",
    "불금",
]

text = 0
count = 0
total = 0.0
text_list = []

for num in list:

    try:
        number_list = float(num)
        count += 1
        total += number_list
    except ValueError:
        text += 1
        text_list.append(num)
        continue

    print(number_list)

print(f"리스트에 숫자가 아닌 값은 {text}개 있습니다. 그 목록 값은 {text_list}입니다.")
print(f"숫자는 {count}개 있으며 총 합은 {number_list:.2f}입니다.")