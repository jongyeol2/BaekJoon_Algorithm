def solution(lottos, win_nums):
    zero = 0
    num = 0
    num_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    for i in lottos:
        if i:
            if i in win_nums:
                num += 1
        else:
            zero += 1
    answer = [num_dict[num+zero], num_dict[num]]
    return answer