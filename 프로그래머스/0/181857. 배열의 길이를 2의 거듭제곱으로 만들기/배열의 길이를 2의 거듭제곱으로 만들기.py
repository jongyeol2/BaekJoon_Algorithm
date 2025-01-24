import math

def solution(arr):
    while not math.log2(len(arr)).is_integer():
        arr.append(0)
    return arr