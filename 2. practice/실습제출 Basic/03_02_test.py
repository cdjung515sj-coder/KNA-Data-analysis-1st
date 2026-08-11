print("=== 실습 - [start:end]로 구간 자르기 ===")
word = "Posco PDM Academy"
print(len(word))  # 17
# "sco PDM A"를 출력하려면?  2:11
print(word[2:11])


# ===============================================
print("\n\n=== 실습 - [:n] start 생략 ===")
word = "Posco PDM Academy"
# 앞 4글자만 추출하기 - 예상 결과: Posc -> [:4]
print(word[:4])


# ===============================================
print("\n\n=== 실습 - [n:] end 생략 ===")
word = "Posco PDM Academy"
# 뒤 5글자만 추출하기 - 예상 결과: ademy -> [12:]
print(word[12:])


# ===============================================
print("\n\n=== 실습 - [-n:] 음수 슬라이싱 (뒤 n글자) ===")
word = "Posco PDM Academy"
# 뒤 2글자만 추출하기(음수 슬라이싱) - 예상 결과: my -> [-2:]
print(word[-2:])


# ===============================================
print("\n\n=== 실습 - step으로 건너뛰기 ===")
word = "Posco PDM Academy"
# 2칸 간격 추출하기 - 예상 결과: PsoPMAaey -> [::2]
print(word[::2])


# ===============================================
print("\n\n=== 실습 - 문자열 뒤집기 ===")
word = "Posco PDM Academy"
# 문자열 - 예상 결과: ymedacA MDP ocsoP -> [::-1]
print(word[::-1])