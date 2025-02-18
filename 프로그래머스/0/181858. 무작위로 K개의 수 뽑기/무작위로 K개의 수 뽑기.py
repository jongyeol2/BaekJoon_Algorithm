def solution(arr, k):
    answer = list(dict.fromkeys(arr))
    if len(answer) > k:
        answer = answer[:k]
        
    while len(answer) != k:
            answer.append(-1)
    return answer