# SILVER4
# 정수 M개가 주어졌을 때, N개 중 이 수가 적혀 있는 숫자 카드는 몇개인지
# 구하는 프로그램 작성
import sys

def binary_search(arr, target, start, end):
    global cnt
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        cnt += 1

    # 하나를 찾더라도 나머지 역시 진행되어야 한다.
    # 오른쪽 부분에 대해 이진 탐색
    binary_search(arr, target, mid+1, end)
    # 왼쪽 부분에 대해 이진 탐색
    binary_search(arr, target, start, mid-1)


N = int(input())
arr1 = sys.stdin.readline().split()
M = int(input())
arr2 = sys.stdin.readline().split()
result = ''

arr1 = sorted(arr1)

print(arr1)

for num in arr2:
    cnt = 0
    binary_search(arr1, num, 0, len(arr1)-1)
    result += str(cnt) + ' '
sys.stdout.write(result)
# 첫번째 제출 : 시간 초과 -> 출력문 만드는 부분 수정해 봄 -> 시간초과
# 두번째 제출 이후 : enumerate 아닌 cnt로 카운팅 -> 이래도 시간초과...
# map 없애고 string 찾는 걸로 변경 -> 시간 초과
# 대박... arr1 정렬을 안했었음 -> 안됨...

