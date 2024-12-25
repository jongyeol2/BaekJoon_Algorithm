import math

def solution(n):
    return abs(n*6) // math.gcd(6,n) / 6
    
    
    
    
#     multiple_6 = set()
#     multiple_n = set()
    
#     for i in range(1, n+1):
#         multiple_6.add(i*6)
#     for i in range(1, 6+1):
#         multiple_n.add(i*n)
    
#     answer = min(multiple_6 & multiple_n) / 6
            
#     return answer