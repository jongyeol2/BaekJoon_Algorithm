def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        sum_n = 0
        now = i
        
        while sum_n < n:
            sum_n += now
            now += 1
        
        if sum_n == n:
            answer += 1
    
    
    # 2번
    # a 부터 b 까지 연속된 자연수 합 공식
    # (b-a+1)*(a+b)/2
    
    # for a in range(1,n+1):
    #     for b in range(a,n+1):
    #         if ((b-a+1)*(a+b)/2) == n:
    #             answer += 1

    
    # 1번
    # for first_hang in range(1,n+1):
    #     sum_suyeol = first_hang
    #     while sum_suyeol <= n:
    #         if sum_suyeol == n:
    #             answer += 1
    #             sum_suyeol += (sum_suyeol+1)
    #             break
    #         sum_suyeol += (sum_suyeol+1)
        
    return answer

