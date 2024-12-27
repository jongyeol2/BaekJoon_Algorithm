import math

def solution(n):
    if math.sqrt(n).is_integer():
        return (math.sqrt(n) + 1)**2
    else:
        return -1