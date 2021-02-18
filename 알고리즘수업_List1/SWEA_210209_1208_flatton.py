# 가로 길이는 항상 100으로 주어진다.
# 평탄화 : 가장 높은 지점을 찾아서, 가장 낮은 부분을 메꾸는 것.
# 가장 높은 부분을 찾고, 가장 낮은 부분을 찾는다.
# 가장 높은 부분은 -1을 하고, 가장 낮은 부분은 +1을 한다.

# 생각해야 할 점 : 최고점 또는 최저점이 복수인 경우에는 어떻게 하는가? -> 등호(=)를 사용하면 해결할 수 있을 것 같다..
for tc in range(1, 11):
    dumps = int(input())
    box_list = list(map(int, input().split()))

    for dump in range(0,dumps):
        max_value = box_list[0]
        min_value = box_list[0]
        max_position = 0
        min_position = 0

        for i, box_height in enumerate(box_list):
            if box_height >= max_value:
                max_value = box_height
                max_position = i
            if box_height <= min_value:
                min_value = box_height
                min_position = i
        # 최저점과 최고점을 찾았으면 평탄화를 시작한다.
        box_list[max_position] -= 1
        box_list[min_position] += 1

    # dump 만큼의 횟수를 반복했으면, 최고점과 최저점의 높이 차를 출력한다.

    # Bubble sort를 이용해서 오름차순으로 정렬할 수도 있다.
    for box_height in box_list:
        for i in range(0,len(box_list)-1): # 마지막은 수행하지 않아도 된다.
            if box_list[i+1] > box_list[i]:
                box_list[i], box_list[i+1] = box_list[i+1], box_list[i]
    print(f'#{tc} {box_list[-1] - box_list[0]}')

    # max_result = box_list[0]
    # min_result = box_list[0]
    # for box_height in box_list:
    #     if box_height >= max_result:
    #         max_result = box_height
    #     if box_height <= min_result:
    #         min_result = box_height
    #
    # result = max_result - min_result
    # print(f'#{tc} {result}')

# Answer!!!

# 함수를 만든 이유 : 모듈화!
def min_search():
    # 임의의 값으로 초기화
    min_value = 987675
    min_idx = -1

    for i in range(len(box)): # box의 길이가 100이다.
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i
    return min_idx

def max_search():
    max_value = 0
    max_idx = -1

    for i in range(len(box)): # box의 길이가 100이다.
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i
    return max_idx

for tc in range(1, 10+1):
    # N = dump 회수
    N = int(input())
    # 박스들..
    box = list(map(int,input().split()))

    # N번 덤프하기 : 평탄화 작업 시작
    for i in range(N):
        # 최고 높이 상자 한칸 내리기
        box[max_search()] -= 1
        # 최저 높이 상자 한칸 올리기
        box[min_search()] += 1

    print(f'#{tc} {box[max_search()] - box[min_search()]}')


# Answer2
# 오름차순으로 박스를 정렬하면 ? 마지막 값이 최고값이 되고, 최초의 값이 최저값이 된다.
# 오름차순 후 마지막 인덱스에 있는 값은 -1, 처음 인덱스에 있는 값은 +1

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1,11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        bubble_sort(box)
        box[0] += 1
        box[-1] -= 1
    bubble_sort(box) # 왜 앞뒤로 2번 해야 하지..?

    print(f'#{tc} {box[max_search()] - box[min_search()]}')

# Answer3
# counting list를 이용해서 풀어보자.
# 박스의 최대 높이가 100이므로, index가 100까지 있는 list를 하나 만들고, 각 높이를 갖는 줄이 몇개 있는지 count
# 최고 높이가 9이고 가장 낮은 높이가 0일때, 박스를 옮기면
# 높이 9를 갖는 줄이 -1, 높이 8을 갖는 줄이 +1되고, 높이 0을 갖는 줄이 -1, 높이 1을 갖는 줄이 +1

for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101 # 박스의 최대 높이가 100

    # Box의 인덱스 자체를 값으로서 활용할 것이다.
    # 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트하면서 최고점과 최저점을 찾아보자.
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value-1: # 최고-최저 간의 차이가 1인 경우에는 덤프를 실행하지 않겠다..
        box[min_value] -= 1
        box[min_value+1] += 1

        box[max_value] -= 1
        box[max_value-1] += 1

        # 포인터를 변경하자..
        if box[min_value] == 0:
            min_value += 1

        if box[max_value] == 0:
            max_value -= 1

        N -= 1 # Dump 회수 줄이기..

    print(f'#{tc} {max_value - min_value}')