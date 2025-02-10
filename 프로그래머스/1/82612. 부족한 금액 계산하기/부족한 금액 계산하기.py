def solution(price, money, count):
    total = (count / 2)*(price + price*count)
    change = money - total
    
    if change >= 0:
        return 0
    else:
        return abs(change)