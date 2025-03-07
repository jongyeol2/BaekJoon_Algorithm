def solution(keyinput, board):
    answer = [0,0]
    x_size = board[0] // 2
    y_size = board[1] // 2
    
    for i in keyinput:
        if i == "left":
            answer[0] += -1
            if answer[0] < -x_size:
                answer[0] = -x_size
        elif i == "right":
            answer[0] += 1
            if answer[0] > x_size:
                answer[0] = x_size
        elif i == "up":
            answer[1] += 1
            if answer[1] > y_size:
                answer[1] = y_size
        elif i == "down":
            answer[1] += -1
            if answer[1] < -y_size:
                answer[1] = -y_size
                        
    return answer