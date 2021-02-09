N = 3
card = [4,5,6]

# 반복문을 이용해서 작성한다.
# 이 3개에 대해서만 run인지 triplet인지 한번 파악해 보자..

run = False
tri = False
for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != j and k != i:
                    print(card[i], card[j], card[k])
                    # run 검사
                    if card[k] == card[j] + 1 and card[j] == card[i] + 1:
                        run = True

                    # triplet 검사
                    if card[i] == card[j] and card[j] == card[k]:
                        tri = True

print(run, tri)