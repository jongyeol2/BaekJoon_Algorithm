def solution(n,a,b):
    match_round = 1
    match = list(range(1, n+1))
    
    if a > b:
        a, b = b, a
    
    while True:
        if (match.index(a) % 2 == 0) and match.index(a) == (match.index(b) - 1):
            return match_round
        else:
            match = [0] * (n//2)
            a = a // 2 + a % 2
            b = b // 2 + b % 2
            match[a-1] = a
            match[b-1] = b
            match_round += 1
        