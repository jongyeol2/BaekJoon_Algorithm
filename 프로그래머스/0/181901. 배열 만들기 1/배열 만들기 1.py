def solution(n, k):
    answer = []
    num = 1
    while k*num <= n:
        answer.append(k*num)
        num += 1
    return answer