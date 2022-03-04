# SILVER1
def solution(s, i, total): # s는 배열, i는 인덱스, total은 합이다.
    global result
    if i == len(s):
        if total not in result:
            result.append(total)
        return

    solution(s, i+1, total + s[i])
    solution(s, i+1, total)


n = int(input())
s = list(map(int, input().split()))
result = []

solution(s, 0, 0)
result = sorted(result)
result.pop(0)

# 이제 가장 작은 자연수를 찾자.


