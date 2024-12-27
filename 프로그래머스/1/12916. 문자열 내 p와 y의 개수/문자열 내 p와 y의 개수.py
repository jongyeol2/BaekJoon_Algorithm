def solution(s):
    sum_p = 0
    sum_y = 0
    for i in s:
        if i in ['p','P']:
            sum_p += 1
            
    for i in s:
        if i in ['y', 'Y']:
            sum_y += 1

    return sum_p == sum_y