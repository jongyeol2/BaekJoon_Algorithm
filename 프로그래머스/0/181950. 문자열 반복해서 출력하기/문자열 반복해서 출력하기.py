str, n = input().strip().split(' ')
n = int(n)

if 1 <= len(str) <= 10 and 1 <= n <= 5 :
    print(str * n)
else :
    print("제한범위에 알맞게 입력하세요")
    