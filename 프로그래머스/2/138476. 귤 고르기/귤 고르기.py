def solution(k, tangerine):
    answer = 0
    cnt = {}

    for i in tangerine:
        cnt[i] = cnt.get(i, 0) + 1
    
    cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
    
    for i in cnt:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
        
    return answer