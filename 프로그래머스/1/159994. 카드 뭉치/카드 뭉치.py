def solution(cards1, cards2, goal):
    num1 = 0
    num2 = 0
    for i in goal:
        if num1 < len(cards1) and i == cards1[num1]:
            num1 += 1
        elif num2 < len(cards2) and i == cards2[num2]:
            num2 += 1
        else:
            return "No"
    return "Yes"