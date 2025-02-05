def solution(s):
    word_list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for num, word in enumerate(word_list):
        s = s.replace(word, str(num))
    return int(s)