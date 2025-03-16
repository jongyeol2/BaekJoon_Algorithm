def solution(dots):
    answer = 0
    x_list, y_list = zip(*dots)
    x = max(x_list) - min(x_list)
    y = max(y_list) - min(y_list)
    
    return x*y