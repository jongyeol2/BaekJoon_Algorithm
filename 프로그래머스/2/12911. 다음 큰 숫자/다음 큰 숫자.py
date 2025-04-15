def solution(n):
    count_1 = str(bin(n)).count("1")
    
    while True:
        n += 1
        if count_1 == str(bin(n)).count("1"):
            break
        
    return n