def solution(dots):
    answer = 0
    list_x = [dots[i][0] for i in range(len(dots))]
    list_y = [dots[i][1] for i in range(len(dots))]
    sorted_dots = sorted(dots, key=lambda x: x[0])
    x_increase_1 = sorted_dots[1][0] - sorted_dots[0][0]
    x_increase_2 = sorted_dots[3][0] - sorted_dots[2][0]
    y_increase_1 = sorted_dots[1][1] - sorted_dots[0][1]
    y_increase_2 = sorted_dots[3][1] - sorted_dots[2][1]
    gradient_1 = y_increase_1 / x_increase_1
    gradient_2 = y_increase_2 / x_increase_2
    
    # 대각 X
    if (len(set(list_x)) == 2 and list_x.count(list_x[0])) or (len(set(list_y)) == 2 and list_x.count(list_y[0])):
        answer = 1
    
    # 대각 O
    if  gradient_1 == gradient_2:
        answer = 1

    return answer