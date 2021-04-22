def select(idx):
    global sel
    global subset
    if idx == N:
        if count_1(sel):
            subset.append(sel)
    else:
        sel[idx] = 1
        select(idx+1)
        sel[idx] = 0
        select(idx+1)

def count_1(arr):
    cnt = 0
    where = []
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt += 1
            where.append(i)
    if cnt == N/2:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())) for _ in range(N)] # 동일 식재료에 대한 시너지는 0
    sel = [0]*N # .선택 여부를 저장하는 리스트
    subset = []
    select(0)
    print(subset)



    S = [list(input().split()