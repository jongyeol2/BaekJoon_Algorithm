def solution(a, b):
    answer = 1
    fract = 1
    
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            fract = i
    
    b2= b // fract

    while b2 % 2 == 0:
        b2 //= 2
    while b2 % 5 == 0:
        b2 //= 5

    if b2 != 1:
        answer = 2
    
    
    return answer