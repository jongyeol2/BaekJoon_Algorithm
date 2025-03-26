def solution(n):
    first_three = make_three(n)
    second_three = first_three[::-1]
    answer = int(second_three, 3)
    
    return answer

def make_three(n):
    if n == 0:
        return "0"
    
    three_n = ""
    while n > 0:
        three_n = str(n % 3) + three_n
        n //= 3
    return three_n