# SILVER2
# 시작 시간순으로 정렬한다.
# 시작 시간과 끝나는 시간의 범위가 int여서 계수 정렬은 사용할 수 없다.
# 병합 정렬을 사용하자.
def merge_sort(arr, start, end):
    # 종료 조건을 설정하자. 리스트의 길이가 1 이하이면 종료한다.
    # 병합 정렬의 전제 조건은 리스트의 길이가 1이면 이미 정렬되어 있다고 가정하는 것이다.
    if len(arr) <= 1:
        return arr

    # 중앙값 먼저 잡자.
    mid = len(arr) // 2

    # 왼쪽 범위, 오른쪽 범위에 대해서 재귀 함수
    left = merge_sort(arr, start, mid - 1)
    right = merge_sort(arr, mid, end)

    # 왼쪽, 오른쪽 합치자.
    pointer1 = 0
    pointer2 = 0

    merged = []
    while pointer1 < len(left) and pointer2 < len(right):
        if left[pointer1] < right[pointer2]:
            merged.append(left[pointer1])
            pointer1 += 1
        else:
            merged.append(right[pointer2])
            pointer2 += 1

    # while문이 끝나면, 남은 대상을 merged에 추가해 준다.
    if pointer1 == len(left):
        while pointer2 < len(right):
            merged.append(right[pointer2])
            pointer2 += 1
    if pointer2 == len(right):
        while pointer1 < len(left):
            merged.append(left[pointer1])
            pointer1 += 1

    return merged


def selection_sort(arr, arr2):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            # st가 같은 경우에는 ? et를 비교해야 한다.
            elif arr[min_index] == arr[j]:
                if arr2[min_index] > arr2[j]:
                    min_index = j
                # 그 이외의 경우에는 그냥 min_index 유지
        arr[min_index], arr[i] = arr[i], arr[min_index]
        # et 또한 변경해야 한다.
        # 문제점 : 만약 st가 같다면...
        arr2[min_index], arr2[i] = arr2[i], arr2[min_index]


N = int(input())
st = []
et = []
for _ in range(N):
    time1, time2 = map(int, input().split())
    st.append(time1)
    et.append(time2)

# merge_sort(st, 0, len(st) - 1) # 단, 주의해야할 점은, et 또한 마찬가지로 해줘야 한다는 점이다.
# 문제점 : et의 인덱스를 기록해 둘 수가 없다...

# 그냥 선택 정렬로 풀자.
selection_sort(st, et)

for start

