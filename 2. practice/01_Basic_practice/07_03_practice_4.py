# 실습 4. 센서 분석 함수 세트 만들기


def avg_values(values):
    return sum(values) / len(values)


def is_over_limit(avg, limit=90):
    if avg > limit:
        return "위험"
    return "정상"


data = [10, 20, 50, 80, 100, 110]
avg = avg_values(data)
result = is_over_limit(avg)

print(f"{avg:.1f} {result}")
