def solution(score):
    answer = [0] * len(score)
    nums = []
    rank = 1
    
    for i, scores in enumerate(score):
        nums.append([i,sum(scores)/2])
    
    sorted_nums = sorted(nums, key=lambda x: x[1], reverse=True)
    
    prev_score = None
    for i, (idx, num) in enumerate(sorted_nums):
        if prev_score != num:
            rank = i + 1
        answer[idx] = rank
        prev_score = num
    
    return answer