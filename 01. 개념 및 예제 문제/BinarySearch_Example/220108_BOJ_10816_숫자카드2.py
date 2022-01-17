# SILVER4
# 시간초과 해법 : card의 중복을 미리 count 해두고 해당하는 card를 이분탐색으로 찾을 때 불러오는 것
# 결국, cnt_list를 출력 안하고 그냥 그때 그때 출력하는 형식으로 하니까 PASS...
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
cardsDic = {}
M = int(input())
nums = list(map(int, input().split()))

for c in cards:
    if c not in cardsDic:
        cardsDic[c] = 1
    else:
        cardsDic[c] += 1

for n in nums:
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == n:
            break
        elif cards[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    if cards[mid] == n:
        print(cardsDic[n], end=" ")
    else:
        print(0, end=" ")

