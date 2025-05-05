a, b = map(int, input().strip().split(' '))
answer = ""

row = "*"*a
for _ in range(b):
    answer += row + "\n"

print(answer)

