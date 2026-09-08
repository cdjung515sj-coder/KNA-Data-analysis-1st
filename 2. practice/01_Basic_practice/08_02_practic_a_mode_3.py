# 실습 3. a 모드로 기존 내용을 지우지 않고 새 기록을 이어 붙이기

with open("data/hi_hello.txt", "a", encoding="utf-8") as f:
    f.write("히히 파일 생성 내가 해냄~")


with open("data/hi_hello.txt", "r", encoding="utf-8") as r:
    r = r.read()
print(r)
