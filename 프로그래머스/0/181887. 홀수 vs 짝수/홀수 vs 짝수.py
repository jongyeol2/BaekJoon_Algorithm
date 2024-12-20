def solution(num_list):
    return max(sum(num_list[0:len(num_list):2]), sum(num_list[1:len(num_list):2]))