# 실습 1. open 으로 파일 읽기

# read로 전체를 한 문자열로 출력
f = open("data/sample.txt", "r", encoding="utf-8")
d = open("data/sample.txt", "r", encoding="utf-8")


read = f.read()
lines = d.readlines()
print(read)
print("-----")
print(lines)

f.close()


print(" ============================")

# 실습 1. with open() 컨텍스트 매니저
# 블록이 끝나면 파일이 자동으로 닫힘 - 실무 기본형태

with open("data/sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)

# 이건 with를 썻기 때문에 닫을 필요 없음
