def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    if before == after:
        answer = 1
    return answer