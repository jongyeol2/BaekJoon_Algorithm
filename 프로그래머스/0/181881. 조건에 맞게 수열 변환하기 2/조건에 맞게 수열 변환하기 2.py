def solution(arr):
    answer = 0
    
    def arr_x(x):
        if (x >= 50) and (x % 2) == 0:
            return x // 2
        elif (x < 50) and (x % 2) == 1:
            return x*2 + 1
        else:
            return x
        
    while True:
        arr_x1 = [arr_x(x) for x in arr]
        if arr_x1 == arr:
            return answer
        arr = arr_x1
        answer += 1
        
    