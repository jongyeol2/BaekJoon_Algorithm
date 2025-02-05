def solution(s):
    answer = 0
    new_s = s.split()
    for i in range(len(new_s)):
        if new_s[i] == "Z":
            answer -= int(new_s[i-1])
        else:
            answer += int(new_s[i])
    return answer