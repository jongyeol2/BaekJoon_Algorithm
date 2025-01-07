def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
        elif ord(i) in range(65,91):
            if ord(i) + n > 90:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        elif ord(i) in range(97,123):
            if ord(i) + n > 122:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
    # 공백은 32
    # A 는 65
    # Z 는 90
    # a 는 97
    # z 는 122
    return answer