def solution(s):
    answer = []
    
    for idx, word in enumerate(s):
        if idx == 0:
            answer.append(-1)
        elif word not in s[:idx]:
            answer.append(-1)
        else:
            place = s[:idx][::-1].index(word) + 1
            answer.append(place)
    
    return answer