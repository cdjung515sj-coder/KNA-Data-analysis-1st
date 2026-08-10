# 조건문 - if
# 항상 실행되지 않고 조건에 따라서 실행되는 코드가 달랐으면 할 때 사용
# 실행되는 코드가 달랐으면 할 때 사용
# 코드가 분기라고도 표현 함.
# 조건문의 조건은 True / False로 결과가 나와야 함. 무조건 무조건이야 ~

# if 조건식:
# \t 실행할 코드 (한 칸 들여쓰기)

# if문의 : (콜론)은 그 다음 올 코드가 if문 조건식의 결과가 True일 때만 실행됨
# 즉, 여기서부터 이 조건에 속한다라는 신호
# ⚠️ 조건에 속하는 코드는 모두 들여쓰기가 적용되어있어야 함


temp = 85
if temp > 80:  # 만약에 temp라는 변수에 담긴 값이 80보다 크다면?
    print("🚨🚨 주의 🚨🚨 : temp 값이 80보다 큽니다.")
    print("⚠️ 관리자를 불러주세요 ⚠️")
print("이건 항상 실행되는 코드")

temp = 50
if (
    temp > 80
):  # 50이 80보다 큰지 비교하고 False라는 결과를 확인하면, 들여쓰기 한 코드는 실행하지 않음
    print("🚨🚨 주의 🚨🚨 : temp 값이 80보다 큽니다.")
    print("⚠️ 관리자를 불러주세요 ⚠️")
print("이건 항상 실행되는 코드")

# temp 변수의 값이 80보다 크다면 "경고" 출력
# temp 변수의 값이 80 이하라면 "정상" 출력
# 위 두 가지의 조건을 모두 하고 싶은 경우

# 방법 1)
# temp = 70일 경우, 방법 1,2 모두 정상 동작
# temp = 90일 경우, 방법 1의 경우 경고만 발생해야되는데 정상까지 출력됨.
if temp > 80:
    print("경고")
print(
    "정상"
)  # if문 밖의 코드는 무조건 실행됨 => 이 경우에는 temp 변수의 값이 80이 넘으면 실행됨.. => 원하는 동작이 아님에도 불구하고 실행이 돼,,,,
# 방법 2) else 사용
if temp > 80:  # if문의 조건이 true일 때만 출력
    print("경고")
else:  # if 문의 조건이 False일 때만 출력
    print("정상")
# if문의 코드블럭과 else문의 코드블럭은 절대 동시에 실행되지 않음
# 둘 중 하나만 실행
# 1개의 분기로 코드를 실행해야할 때 사용함.


# or 연산자 + if 문 중첩
color = input("신호등 색을 입력해주세요.(빨간색, 초록색만 입력 가능) :")
if color == "초록색" or color == "빨간색":
    #  color가 "초록색"이거나 "빨간색"일 때만 실행
    if color == "초록색":
        print("건너세요")  # 중첩 if문은 들여쓰기 더더욱 주의
    # if color == "빨간색": # else문과 동일하게 동작
    # print("기다리세요") # 하지만 else를 사용하는게 효율적
    else:
        print("기다리세요")
    # 사용자 입력값이 "초록색" 이거나 "빨간색"일 때 무조건 출력
    print("이것은 사용자 입력값이 '초록색' 이거나 '빨간색'일 때 무조건 출력됩니다.")
else:
    print("다시 입력하세요")

# and 연산자 + 중첩
# 사람 체온 판단
# 정상 체온 범위 : 36.2~36.9

user1 = float(input("체온을 입력해주세요. :"))

# 1. 첫 번째 if-else 구조 (수정: 들여쓰기 오타 해결)
if user1 >= 36.2 and user1 <= 36.9:
    print("당신은 정상체온입니다.")
else:
    if user1 > 36.9:
        print("당신은 열이 나고 있습니다.")
    else:
        print("당신은 저체온입니다.")

# 2. 두 번째 중첩 if문 구조 (수정: IndentationError가 발생하던 들여쓰기 공백 정돈)
if user1 <= 36.2 or user1 >= 36.9:
    if user1 > 36.9:
        print("당신은 열이 나고 있습니다.")
        if user1 > 37.8:
            print("당신은 고온입니다. 병원에 방문하세요")
        else:
            print("당신은 미열입니다. 조심하세요")
    else:
        print("당신은 저체온입니다.")
else:
    print("당신은 정상체온입니다.")


# elif
# else와 if만으로 분기하기엔 불편하고
# if 중첩이 많아져서 생김

# 3. elif 구조 (수정: 36.2 미만을 저체온으로 지정하여 36.2도 정상체온 구간 보호)
if user1 < 36.2:
    print("당신은 저체온입니다.")
elif user1 >= 36.9 and user1 < 37.8:
    print("당신은 미열입니다. 주의하세요.")
elif user1 >= 37.8:
    print("당신은 고온입니다. 병원 가")
else:
    print("당신은 정상체온입니다.")

print("체온 확인 완료")


# elif 순서

score = 50

if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
elif score >= 50:
    print("미흡")
else:
    print("비상")
# 정상적으로 미흡이 잘 출력됨

score = 100

if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
elif score >= 50:
    print("미흡")
else:
    print("비상")
# 100 이기 때문에 우수가 출력되어야 하나, 코드의 순서가 적합하지 않아 "미흡"이 출력됨.

score = 82

if score >= 90:
    print("우수")  # 거짓
elif score >= 70:
    print("보통")  # 참 => 실행
elif score >= 50:
    print("미흡")
else:
    print("비상")

# if문은 줄바꿈을 하지 않아도 : 을 ㅣ준으로 동작 자체는 가능
# 하지만 줄바꿈해서 가독성을 높이길 권장
# tab은 아직 위의 코드가 끝나지 않았고 한 줄이라는 것을 명시

# score = 82
# if score >= 90: print("우수")
# elif score >= 70: print("보통")
# elif score >= 50: print("미흡")
# else: print("비상")


# not 연산자
# not은 괄호로 감싸서 사용한다.
if not (3 == 5):
    print("출력됨")
# 3과 5는 같지 않으니 False가 되나
# 앞에 not 이 있어서 False를 True로 뒤집어 if가 인식


