# set
# 자동 중복 제거
# 순서가 없음
# 형태가 중괄호로 감쌈

# 빈 set 만들기
empty_list = []  # 빈 리스트
print(type(empty_list))  # <class 'list'>

empty_tuple = ()  # 빈 튜플
print(type(empty_tuple))  # <class 'tuple'>

empty_set = {}
print(type(empty_set))  # <class 'dict'>
# 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
real_empty_set = set()
print(type(real_empty_set))  # <class 'set'>

# 값을 포함한 셋 만들기
logs = ["S01", "S02", "S01", "S03", "S01"]

# 리스트를 {}에 감쌀 경우
# unique = {logs}
# print(type(unique))

# 🚨🚨 print(type(unique)) # TypeError: cannot use 'list' as a set element (unhashable type: 'list')

# 복수의 값을 중괄호에 깜싸 작성
unique = {"S01", "S02", "S01", "S03", "S01"}
print(type(unique))  # <class 'set'>
print(unique)  # {'S01', 'S03', 'S02'}

# set() 사용
unique = set(logs)
print(type(unique))  # <class 'set'>
print(unique)  # {'S03', 'S01', 'S02'}
# unique 셋에는 기존 중복된 값은 제거 된 후 출력
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만, 셋은 순서가 없는 값의 묶음
# 셋은 순서가 없다.

# 🚨🚨 print(unique[0]) # TypeError: 'set' object is not subscriptable
# set에서 인덱스 사용 시 Error 발생

# set에 바로 여러 값을 작성
unique = set(["S01", "S02", "S01", "S03", "S01"])
print(type(unique))  # <class 'set'>
print(unique)  # {'S03', 'S01', 'S02'}

# set을 사용해서 리스트에 들어있는 unique 값의 종류 수를 알 수 있음
print(len(unique))  # 3


# ===========================================

# 셋에 값 추가하기
# 셋.add(추가할 값)
# 이미 있는 값을 추가할 경우 무시함

alerts = {"S01", "S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용해서 추가
alerts.add("S03")
print(alerts)  # {'S01', 'S02', 'S03'}

# S01 에서 또 경고가 발생
# 이미  S01은 경고가 발생한 적이 있고 Alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관 없이
# 이럴 때 set을 쓰면 편리함
alerts.add("S01")
print(alerts)
# S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는 아주 편리함

