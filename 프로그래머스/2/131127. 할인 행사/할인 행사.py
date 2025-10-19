def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        d_list = discount[i:i + 10]
        d_dict = {}
        
        for i in d_list:
            if i in d_dict:
                d_dict[i] += 1
            else:
                d_dict[i] = 1
        
        if want_dict == d_dict:
            answer += 1
    
    return answer