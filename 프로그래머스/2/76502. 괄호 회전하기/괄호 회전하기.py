def solution(s):
    answer = 0
    pairs = {"}": "{", "]": "[", ")": "("}
    
    for i in range(len(s)):
        check = s[i:] + s[:i]
        stack = []
        valid = True
        
        for j in check:
            if j in "({[":
                stack.append(j)
            else:
                if not stack or stack[-1] != pairs[j]:
                    valid = False
                    break
                stack.pop()
            
        if valid and not stack:
            answer += 1

    return answer