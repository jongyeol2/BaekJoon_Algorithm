def solution(n):
    answer = 0
    for x in range(1, n+1):
        cnt = 0
        for i in range(1,x+1):
            if x % i == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer