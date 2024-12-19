def solution(hp):
    a = hp // 5
    b = (hp % 5) // 3
    c = ((hp % 5) % 3) // 1
    # if hp % 5 == 0:
    #     return a
    # elif (hp % 5) % 3 == 0:
    #     return a + b
    # else:
    return a + b + c