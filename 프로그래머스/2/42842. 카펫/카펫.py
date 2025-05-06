def solution(brown, yellow):
    pairs = []
    
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            pairs.append((i, yellow // i))
    
    for i in pairs:
        a, b = i
        if (a+2) * (b+2) == brown + yellow:
            x = max(a+2, b+2)
            y = min(a+2, b+2)
            answer = [x,y]
    
    
    return answer