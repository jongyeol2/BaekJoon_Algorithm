def solution(price, money, count):
    total = 0
    for i in range(1,count+1):
        total += price*i
    
    if (money - total) >= 0:
        answer = 0
    else:
        answer = abs(money-total)
    
    return answer