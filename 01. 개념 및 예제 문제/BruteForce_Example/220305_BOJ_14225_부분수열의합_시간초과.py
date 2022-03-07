# SILVER1
# 아래의 풀이는 pypy3, python3 모두로 해도 시간초과가 발생한다.
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

# 이제 가장 작은 자연수를 찾자.
check_num = [i for i in range(1, result[-1]+2)]
for num in check_num:
    if num not in result:
        print(num)
        break

