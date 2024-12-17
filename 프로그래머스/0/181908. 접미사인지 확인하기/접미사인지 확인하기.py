def solution(my_string, is_suffix):
    if my_string[len(my_string)-len(is_suffix):] == is_suffix:
        return 1
    return 0