def solution(my_string, is_prefix):
    if is_prefix == my_string[:len(is_prefix)]:
        return 1
    return 0