def solution(numbers):
    sort_num = sorted(numbers, reverse=True)
    max1, max2 = sort_num[:2]
    return max1 * max2