# GOLD5
# 참고 코드 : https://hongcoding.tistory.com/3
N, C = map(int, input().split())

array = []
for i in range(N):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0] # 현재 설치한 집을 뜻한다.
        count = 1 # 공유기를 설치한 집 수

        # 두번째 집부터 마지막 집까지 점건한다.
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)