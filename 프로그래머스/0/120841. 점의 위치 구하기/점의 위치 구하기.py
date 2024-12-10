def solution(dot):
    x,y = dot
    if x*y > 0:
        if x > 0:
            answer = 1
        else:
            answer = 3
    else:
        if x > 0:
            answer = 4
        else:
            answer = 2
    return answer