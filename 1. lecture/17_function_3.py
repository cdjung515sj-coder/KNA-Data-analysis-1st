# 07_03 함수 설계와 활둉


# 기본값 인자
def report():
    print("...")


report()


def report(name, value):
    print(f"{name} : {value}")


report("압축기A", 75.3)
