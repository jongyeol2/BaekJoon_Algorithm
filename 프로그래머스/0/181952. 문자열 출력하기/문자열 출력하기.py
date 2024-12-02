str = input()

if 1 <= len(str) and len(str) <= 1000000 :
    print(str)
elif len(str) < 1 :
    print("공백은 입력이 불가합니다.")
elif len(str) > 1000000 :
    print("글자 수 제한 초과입니다.")
