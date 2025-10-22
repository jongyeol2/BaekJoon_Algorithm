def solution(number, limit, power):
    answer = 0
    
    for n in range(1, number + 1):
        divisor = 0
        i = 1
        
        while i * i <= n:
            if n % i == 0:
                if i == (n // i):
                    divisor += 1
                else:
                    divisor += 2
            i += 1
            
        if divisor > limit:
            divisor = power

        answer += divisor
            

    return answer

#     시간초과 풀이
#
#     for i in range(1, number + 1):
#         divisor = 0
        
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 divisor += 1
        
#         if divisor > limit:
#             divisor = power
        
#         answer += divisor