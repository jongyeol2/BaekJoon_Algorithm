def solution(n):
    fac = 1
    i = 1
    while fac <= n:
        i += 1
        fac *= i
        
    return i-1