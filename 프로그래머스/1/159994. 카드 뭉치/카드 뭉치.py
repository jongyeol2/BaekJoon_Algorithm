# def solution(cards1, cards2, goal):
#     num1 = 0
#     num2 = 0
#     for i in goal:
#         if i == cards1[num1]:
#             num1 += 1
#         elif i == cards2[num2]:
#             num2 += 1
#         else:
#             return "No"
#     return "Yes"

def solution(cards1, cards2, goal):
    num1, num2 = 0, 0
    for i in goal:
        # cards1의 현재 단어가 i와 일치하는지 확인
        if num1 < len(cards1) and cards1[num1] == i:
            num1 += 1
        # cards2의 현재 단어가 i와 일치하는지 확인
        elif num2 < len(cards2) and cards2[num2] == i:
            num2 += 1
        # 어느 쪽에서도 사용 불가하면 "No" 반환
        else:
            return "No"
    return "Yes"