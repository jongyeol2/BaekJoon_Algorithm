def solution(my_string):
    
    # a = list(set(my_string))
    # return ''.join(a)
    
    
    
    a = list(dict.fromkeys(my_string))
    return ''.join(a)