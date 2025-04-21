def F(n):
    pibo = [0,1]
    
    for i in range(2,n+1):
        pibo.append(pibo[i-1] + pibo[i-2])
    return pibo[-1]


def solution(n):
    answer = F(n) % 1234567
    return answer