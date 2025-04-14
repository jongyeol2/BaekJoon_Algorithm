def solution(picture, k):
    answer = []
    for i in picture:
        lines = ''.join(j*k for j in i)
    
        for _ in range(k):
            answer.append(lines)
    
    return answer