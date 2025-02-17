def solution(lottos, win_nums):
    num_dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    num = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
              
    answer = [num_dict[num+zero], num_dict[num]]
    return answer