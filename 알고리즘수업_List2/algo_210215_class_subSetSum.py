bit = [0,0,0,0]

# 부분 집합 만드는 방법 1
for i in range(2): # 0 또는 1
    bit[0] = i
    for j in range(2): # 0 또는 1
        bit[1] = j
        for k in range(2): # 0 또는 1
            bit[2] = k
            for l in range(2): # 0 또는 1
                bit[3] = l
                print(*bit)

# 2진수를 나타낸 것으로, 0에서 15까지의 수를 이진법으로 표현한 것이다.
# 반복문 하나로 모든 부분집합의 수를 볼 수는 없을까?


# 부분집합 만드는 방법 2

# 예제 1
arr = [3,6,7,1,5,4]
n = len(arr)
for i in range(1<<n): # i는 0부터 2**6 - 1까지의 값을 갖는다.
    # 각각의 부분집합 케이스에 대해서,,
    for j in range(n): # n은 배열의 크기이다. 따라서 j는 배열 내 index를 의미한다.
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소를 출력한다.
            print(arr[j],end=", ")
print()


# 예제 2
재료 = ['계란', '치즈', '떡']
N = 3
for i in range(1<<N): # 모든 부분집합의 개수
    ans = ""
    for j in range(N): # j는 0,1,2가 된다.
    # 해당 재료가 있는지 없는지를 검사하자
        if i & (1<<j):
            ans += 재료[j] + " "

    print(ans, "라면입니다.")
