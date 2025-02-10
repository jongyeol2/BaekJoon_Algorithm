def solution(price, money, count):
    total = count*(price + price*count) / 2
    change = money - total
    
    if change >= 0:
        return 0
    else:
        return abs(change)