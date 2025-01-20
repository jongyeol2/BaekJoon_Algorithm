def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    answer = sorted(answer)
    return "".join(answer)