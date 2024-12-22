def solution(array, n):
    
#     중복값 판별할때
#     정렬하거나
    
#     세트와 튜플길이 비교하거나
#     음
#     딕셔너리 밸류값들 찾아와서 비교하거나
    
#     고차함수써야하나
    
#     다 안단순한데
    
    
#     3 10 28   20
    
#     17 10 8
    
#     5  3  7  9  1  일때  엔 4 면
    
#     1 3 5 7 9
#     3 1 1 3 5
#     3 
   

    list = []
    array.sort()
    
    for i in array:
        list.append(abs(n-i))
    
    answer = [array[list.index(min(list))]]
    
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
    
    

    
    
    