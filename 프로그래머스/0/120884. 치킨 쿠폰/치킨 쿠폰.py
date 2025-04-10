def solution(chicken):
    service = 0
    coupon = chicken
    
    
    while coupon >= 10:
        free = coupon // 10
        service += free
        coupon = coupon % 10 + free
        
        
        
        # cp_chicken = cp_total // 10
        # cp_rest = cp_total % 10
        # cp_total = cp_rest + cp_rest
        # answer += cp_chicken
    return service