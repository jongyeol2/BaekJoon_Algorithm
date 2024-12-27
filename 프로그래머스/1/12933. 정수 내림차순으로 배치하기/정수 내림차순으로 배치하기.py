def solution(n):
    n = [i for i in str(n)]
    n = sorted(n, reverse=True)
    return int(''.join(n))