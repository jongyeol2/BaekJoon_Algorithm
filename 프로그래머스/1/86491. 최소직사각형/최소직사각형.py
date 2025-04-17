def solution(sizes):
    answer = 0
    size_sorted = []
    lengths = []
    widths = []
    
    for size in sizes:
        if size[0] < size[1]:
            size = size[::-1]
        size_sorted.append(size)
    
    for size in size_sorted:
        lengths.append(size[0])
        widths.append(size[1])
    
    
    return max(lengths) * max(widths)