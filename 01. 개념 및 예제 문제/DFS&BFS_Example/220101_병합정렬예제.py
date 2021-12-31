arr = [37, 10, 22, 30, 35, 13, 25, 24]

def merge_sort(arr, start, end):
    # 끝 조건 설정
    if len(arr) <= 1: # 1보다 리스트의 길이가 작아지는 경우는 어떤 경우지?
        return arr

    mid = len(arr) // 2

    # 계속 분할한다. 리스트의 길이가 0 또는 1이 될 때까지
    left = merge_sort(arr[:mid], arr[start], arr[mid-1])
    right = merge_sort(arr[mid:], arr[mid], arr[end])

    # divide가 끝났으면, merge 해주자.
    # 이 과정에서 순서대로 넣어야 한다.
    pointer1 = 0 # pointer1의 끝은 left 리스트의 마지막 인덱스이다.
    pointer2 = 0 # pointer2의 끝은 right 리스트의 마지막 인덱스이다.

    merged = []
    while pointer1 != len(left) and pointer2 != len(right): # 둘다 리스트의 길이만큼 인덱스가 이동했다는건, 배열 내 모든 원소를 merge했다는 뜻
        if left[pointer1] < right[pointer2]:
            merged.append(left[pointer1])
            pointer1 += 1
        else:
            merged.append(right[pointer2])
            pointer2 += 1

    return merged

