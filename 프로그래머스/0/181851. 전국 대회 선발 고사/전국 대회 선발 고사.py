def solution(rank, attendance):
    answer = []
    for i in range(1, len(rank)+1):
        idx = rank.index(i)
        if attendance[idx]:
            answer.append(idx)
        if len(answer) == 3:
            break
    result = 10000*answer[0] + 100*answer[1] + answer[2]
    
    return result