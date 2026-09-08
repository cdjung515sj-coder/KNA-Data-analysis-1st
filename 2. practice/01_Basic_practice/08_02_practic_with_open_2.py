# 실습 2. with open 으로 파일 쓰기

f = open("data/hi_hello.txt", "w", encoding="utf-8")

with open("data/hi_hello.txt", "w", encoding="utf-8") as f:
    f.write("write를 사용해서 글 작성! 줄 바꿈도 여기서 \n")

r = open("data/hi_hello.txt", "r", encoding="utf-8")
read = r.read()
r.close()
print(read)
