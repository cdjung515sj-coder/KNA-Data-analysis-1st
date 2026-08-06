# 실습 1. open 으로 파일 읽기

# read로 전체를 한 문자열로 출력
f = open("data/sample.txt", "r", encoding="utf-8")

read = f.read()
print(read)

f.close()


# readlines로 줄 리스트로 읽어 출력하기
with open("data/sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)

# 이건 with를 썻기 때문에 닫을 필요 없음
