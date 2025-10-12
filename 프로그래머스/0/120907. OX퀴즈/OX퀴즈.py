def solution(quiz):
    answer = []
    for i in quiz:
        q = i.replace("=", "==")
        if eval(q):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer