def solution(a, b, c, d):
    answer = 0
    a, b, c, d = sorted([a, b, c, d])
    num_set = {a, b, c, d}
    num_list = [a, b, c, d]
    
    if len(num_set) == 1:
        answer = 1111 * a
    elif len(num_set) == 2:
        if a == b and c == d and b != c:
            answer = (a + c)*abs(a - c)
        else:
            for i in num_list:
                if num_list.count(i) == 3:
                    p = i
                elif num_list.count(i) == 1:
                    q = i
            answer = (10 * p + q)**2
    elif len(num_set) == 3:
        q, r = [i for i in num_list if num_list.count(i) == 1]
        answer = q * r
    elif len(num_set) == 4:
        answer = a

    return answer