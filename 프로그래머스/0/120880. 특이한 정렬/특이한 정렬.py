def solution(numlist, n):
#     answer = []
#     numlist_sorted = sorted(numlist)
#     target = numlist.index(n)
    
#     while len(answer) < len(numlist):
#         if numlist_sorted
    
    
#     return numlist
    
    return sorted(numlist, key=lambda x: (abs(x - n), -x))