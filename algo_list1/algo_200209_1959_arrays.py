# Interval 문제와 유사하다.
# 길이가 긴 쪽의 array에서 interval을 짧은 쪽 배열의 길이로 두고, 선택하여 하나씩 곱하면 된다.

case = int(input())
for tc in range(1, case + 1):
    length_info = list(map(int, input().split()))

    # 긴쪽을 기준으로 잡아야 한다.
    if length_info[0] > length_info[1]:
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
    else:
        arr2 = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))

    results = []
    # arr1은 무조건 긴 배열이고, arr2는 무조건 짧은 배열이다.
    interval = len(arr2)
    for i in range(0, len(arr1)-interval+1):
        sum = 0
        temp_arr = arr1[i:interval+i]
        for i,num in enumerate(temp_arr):
            sum += num * arr2[i]
        results.append(sum)

    # result 중에서 가장 큰 값을 반환하면 된다.
    max = 0
    for result in results:
        if result > max:
            max = result
    print(f'#{tc} {max}')