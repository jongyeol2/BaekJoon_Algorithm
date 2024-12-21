def solution(numbers):
    numbers.sort()
    answer = max(numbers[-1]*numbers[-2], numbers[0]*numbers[1])
        
    return answer