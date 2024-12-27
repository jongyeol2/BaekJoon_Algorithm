def solution(x):
    num = 0
    for i in str(x):
        num += int(i)
    
    return (x % num) == 0