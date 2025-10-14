def solution(n, words):
    used = set()
    used.add(words[0])
    
    for i in range(1, len(words)):
        prev = words[i -1]
        curr = words[i]
        
        if curr in used:
            return [(i % n) + 1, (i // n) + 1]
        
        if prev[-1] != curr[0]:
            return [(i % n) + 1, (i // n) + 1]
        
        used.add(curr)

    return [0,0]