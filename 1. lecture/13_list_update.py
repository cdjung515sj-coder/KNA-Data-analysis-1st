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
