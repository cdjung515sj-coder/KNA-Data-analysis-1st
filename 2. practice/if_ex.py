anna=input("안나가 낼 것을 입력해주세요 : ")
hoo=input("후가 낼 것을 입력해주세요 : ")
if(anna=="가위"):
    if(hoo=="가위"):
        print("무승부")
    elif(hoo=="바위"):
        print("후가 이김")
    else:
        print("안나 이김")
elif(anna=="바위"):
    if(hoo=="바위"):
        print("무승부")
    elif(hoo=="보"):
        print("후가 이김")
    else:
        print("안나 이김")
elif(anna=="보"):
    if(hoo=="보"):
        print("무승부")
    elif(hoo=="가위"):
        print("후가 이김")
    else:
        print("안나 이김")
else:
    print("뭐하누;")