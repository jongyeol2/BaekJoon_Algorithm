def solution(sides):
    answer = 0
    
    for i in range(max(sides)-min(sides), sum(sides)+1):
        if (max(sides) - min(sides) < i) and (i <= max(sides)):
            answer += 1
        elif (max(sides) < i) and (i < sum(sides)):
            answer += 1
    return answer