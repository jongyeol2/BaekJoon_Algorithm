def solution(d, budget):
    answer = 0
    d = sorted(d)
    num = 0
    
    for i in d:
        if (num + i) <= budget:
            num += i
            answer += 1
        if num >= budget:
            break
    return answer