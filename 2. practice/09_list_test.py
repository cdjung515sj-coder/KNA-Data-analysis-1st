# 실습 1. 나만의 데이터 리스트 만들기
today_temps = [34,35,32,30,29]
print(today_temps)
print(len(today_temps))
empty = []
print(len(empty))

# 실습 2. 인덱스로 값 꺼내기
list6 = [11,-2,44,13,5,-10]
print(list6[0])
print(list6[2])
print(list6[-1])
print(len(list6)) # 6
print(list6[5]) # 6개니까 마지막 요소는 6-1 = 5

# 실습 3. 인덱스로 꺼낸 값 계산하기
list6 = [11,-2,44,13,5,-10]
first = list6[0]
last = list6[-1]
sum = first+last
print(sum)
print(sum/2)