def solution(k, score):
    answer = []
    honor = []
    
    for i in score:
        honor.append(i)
        honor = sorted(honor, reverse=True)[:k]
        
        answer.append(honor[-1])

    return answer