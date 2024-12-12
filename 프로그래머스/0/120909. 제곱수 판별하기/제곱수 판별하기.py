def solution(n):
    answer = 2
    for i in range(1,n+1):
        if i**2 == n:
            answer = 1
            break
        if i**2 > n:
            break
    return answer