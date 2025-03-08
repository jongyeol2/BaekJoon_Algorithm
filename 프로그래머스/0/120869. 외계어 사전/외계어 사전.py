def solution(spell, dic):
    for word in dic:
        word_list = list(word)
        for i in spell:
            if i in word_list:
                word_list.remove(i)
        if (len(spell) == len(word)) and (not word_list):
            return 1
    return 2