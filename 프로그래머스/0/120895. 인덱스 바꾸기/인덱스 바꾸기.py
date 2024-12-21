def solution(my_string, num1, num2):
    my_string = list(my_string)
    str1 = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = str1
    return ''.join(my_string)