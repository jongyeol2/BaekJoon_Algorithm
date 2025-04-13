def solution(my_string, queries):
    my_string = list(my_string)
    for i in queries:
        s, e = i
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)