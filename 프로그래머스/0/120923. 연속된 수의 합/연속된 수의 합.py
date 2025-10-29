def solution(num, total):
    answer = []
    
    if num % 2 == 0:
        n = (total - sum(list(range(num)))) // num
        answer = list(range(n, n+num))
        
        pass
    else:
        median = total // num
        n = num // 2
        answer = [i for i in range(median-n, median+n+1)]
    
    
    return answer