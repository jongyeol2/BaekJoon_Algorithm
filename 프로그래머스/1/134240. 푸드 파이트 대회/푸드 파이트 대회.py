def solution(food):
    side = ""
    
    for i in range(1,len(food)):
        if food[i] == 1:
            continue
        side += str(i)*(food[i]//2)
    
    answer = side + "0" + side[::-1]
    
    return answer