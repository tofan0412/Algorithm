# 고지식한 알고리즘
# 시간복잡도 : Big-Oh Notation : O(MN)

# 1. while을 이용해서,,
t = "this is a book!"
p = "is"

i = 0 # 기준 str의 pointer
j = 0 # keyword의 pointer
while j < len(p) and i < len(t):
    if t[i] != p[j]: # 단어가 일치하지 않는 경우
        i = i - j # 마찬가지로 기준 str의 포인터를 다시 일치하지 않는 단어로 옮긴다.
        j = -1 # keyword의 pointer를 다시 처음으로 돌린다.
    i += 1
    j += 1

if j == len(p): # keyword 위의 포인터가 끝까지 갔다는 뜻으로, 기준 str내 동일한 단어가 있다는 뜻이다.
    print("일치하는 항목이 존재합니다.")
else:
    print("일치하는 단어가 존재하지 않습니다.")

# 2. for를 이용해서

for i in range(len(t) - len(p) + 1): # N-M+1을 하지 않으면, 하단의 for문에서 range가 기준 str을 넘어갈 수 있다.
    cnt = 0
    for j in range(len(p)):
        if t[i+j] == p[j]:
            cnt += 1
        else:
            break
    if cnt == len(p):
        print("일치하는 항목이 존재합니다..")