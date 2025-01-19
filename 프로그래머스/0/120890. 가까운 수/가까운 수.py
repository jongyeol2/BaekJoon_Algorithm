def solution(array, n):
    list = []
    array.sort()
    
    for i in array:
        list.append(abs(n-i))
    
    answer = [array[list.index(min(list))]]
    
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
    
    

    
    
    