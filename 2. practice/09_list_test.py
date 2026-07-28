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

# 실습 4. 슬라이싱으로 구간 자르기
temps = [10,20,30,40,50,60,70,80,90,100]
print(temps[:3])
print(temps[-3:])
print(len(temps[:3]),len(temps[-3:]))

# 실습 5. 데이터를 두 구간으로 나누기
list12 = [1,2,3,4,5,6,7,8,9,10,11,12]
first = list12[:6]
second = list12[6:]
print(first)
print(second)
print(len(first),len(second))