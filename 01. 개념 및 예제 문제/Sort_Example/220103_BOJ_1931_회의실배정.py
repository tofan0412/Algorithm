# SILVER2
# 시작 시간과 끝나는 시간의 범위가 int여서 계수 정렬은 사용할 수 없다.

# 단순히 시작 시간 기준으로 빠른 순서대로 정렬한 함수
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
selection_sort(st, et)

result = -1
for i in range(len(st)):
    stack = []
    stack.append([st[i], et[i]])
    count = 1
    pointer = i+1
    while pointer < len(st):
        now = stack.pop()
        if now[0] <= st[pointer] < now[1]:
            # 다시 도로 넣는다.
            stack.append(now)
            pointer += 1
            continue
        else:
            stack.append([st[pointer], et[pointer]])
            count += 1
            pointer += 1
    if result < count:
        result = count

print(result)

# 결과 : 시간초과