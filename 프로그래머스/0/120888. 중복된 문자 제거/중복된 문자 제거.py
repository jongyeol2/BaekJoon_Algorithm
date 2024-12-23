def solution(my_string):
    a = list(dict.fromkeys(my_string))
    return ''.join(a)