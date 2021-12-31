# BRONZE1
N = int(input())
arr = []
for _ in range(N):
    number = int(input())
    arr.append(number)

# 1. 선택 정렬을 이용하여 오름차순으로 정렬하세요.
# 선택정렬 :  1 ~ N-1번째 수를 탐색하여 최소값을 0번째 인덱스에, 2 ~ N-1번째 수를 탐색하여 최소값을 1번째 인덱스에, ...
# for i in range(N):
#     min_index = i
#     for j in range(i+1, N):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[min_index], arr[i] = arr[i], arr[min_index]

# 2. 버블 정렬을 이용하여 오름차순으로 정렬하세요.
# for i in range(N):
#     for j in range(0, N-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]


# 3. 삽입 정렬을 이용하여 오름차순으로 정렬하세요.
# 삽입 정렬 : 첫번째 원소는 정렬이 완료된 원소라 가정한다.
for i in range(N-1):
    for j in range(i+1, 0, -1):
        # 왼쪽에 있는 원소보다 오른쪽에 있는 원소가 작다면 순서를 바꿔준다.
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        # 그렇지 않다면 넘어간다.
        else:
            break

for number in arr:
    print(number)
