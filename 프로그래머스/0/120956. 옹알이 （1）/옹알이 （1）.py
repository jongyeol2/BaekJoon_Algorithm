def solution(babbling):
    answer = 0
    possible_pronounce = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for pp in possible_pronounce:
            if pp * 2 in word:
                break
            elif pp in word:
                word = word.replace(pp, " ")
        if word.strip() == "":
            answer += 1
    return answer