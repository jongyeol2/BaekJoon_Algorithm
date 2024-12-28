def solution(date1, date2):
    if date2[0] > date1[0]:
        return 1
    elif date2[0] == date1[0] and date2[1] > date1[1]:
        return 1
    elif date2[1] == date1[1] and date2[2] > date1[2]:
        return 1
    return 0