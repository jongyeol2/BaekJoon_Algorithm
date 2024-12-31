def solution(balls, share):
    n = balls
    m = share
    
    # (n-m)!
    a = 1
    for i in range(1,(n-m)+1):
        a *= i
    
    # n!/m!
    b = 1
    for i in range(n-m):
        b *= (n-i)
 
    return b/a