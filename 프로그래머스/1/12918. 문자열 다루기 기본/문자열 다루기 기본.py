def solution(s):
    answer = False
    if len(s) in [4, 6] and s.isdigit():
        answer = True
    return answer