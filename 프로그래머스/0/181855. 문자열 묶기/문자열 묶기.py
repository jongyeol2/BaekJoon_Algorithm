from collections import Counter

def solution(strArr):
    
    for idx, i in enumerate(strArr):
        strArr[idx] = len(i)
    
    counter = Counter(strArr)
    
    return max(counter.values())