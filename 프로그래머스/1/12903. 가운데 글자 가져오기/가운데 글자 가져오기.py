def solution(s):
    a = len(s)
    if len(s) % 2 == 1:
        answer = s[int(a/2)]
    else:
        answer = s[int(a/2)-1:int(a/2)+1]
    return answer