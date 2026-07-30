# 기존 배열의 모든 요소에 3을 곱한 값을 가진 새 리스트 작성
temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temps:
    doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 새 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3]
low = []
high = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print(f"high: {high}")
print(f"low: {low}")

# 복습) sort() : 원본 배열을 오름차순으로 정렬해줌
# 하지만 반환해주기 않기 때문에 print로 바로 찍으면 None 출력
print(low.sort())

# 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)


# 리스트 안의 리스트
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터
# 바깥 대괄호를 "행", 안쪽 인덱스 리스트를 "열"

print(rows[0])  # ['펌프', 25]
print(type(rows[0]))  # <class 'list'>
print(type(rows))  # <class 'list'>

# 중첩된 리스트 안의 값에 접근하고 싶다면?
print(rows[1][1]) # 32
# 1. rows[1]을 찾음 -  ["모터", 32]
# 2. print(["모터", 32][1]) -> [1] 앞의 리스트에서 1번 인덱스 값에 접근
# 3. print(32) -> 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러번 이어서 접근

# 리스트 안의 리스트 온도값만 출력하기
for row in rows:
    print(row[0],"온도",row[1]) # 펌프 온도 25
# rows는 리스트를 담고 있는 큰 리스트
# row는 rows 안에 있는 작은 리스트 예) ["펌프", 25] 하나
