# SILVER1
# 수열 S가 주어졌을 때 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오
# 예를 들어 S = [5, 1, 2]인 경우에 나올 수 있는 합은
# 1, 2, 3, 5, 6, 7, 8을 만들 수 있다.
# 하지만 4는 만들 수 없기 때문에 답은 4이다.

def solution(s, i, total): # s는 배열, i는 인덱스, total은 합이다.
    global result
    if i == len(s):
        if total not in result:
            result.append(total)
        return

    # 1. 현재 인덱스의 수를 선택한다.
    solution(s, i+1, total + s[i])
    # 2. 현재 인덱스의 수를 선택하지 않는다.
    solution(s, i+1, total)


n = int(input())
s = list(map(int, input().split()))

result = []
solution(s, 0, 0)

# 0은 반드시 존재하므로 제외한다. (모든 원소를 선택하지 않은 경우)
result.pop(result.index(0))

# 이제 가장 작은 자연수를 찾자.
# 처음에는 1부터 해서 있는지 없는지 검사함 => 시간초과
