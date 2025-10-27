def solution(clothes):
    answer = 1
    category = {}
    
    for clothe in clothes:
        if clothe[1] in category:
            category[clothe[1]] += 1
        else:
            category[clothe[1]] = 1
    
    case = list(category.values())
    
    for i in case:
        answer *= (i + 1)
    
    answer -= 1
    return answer