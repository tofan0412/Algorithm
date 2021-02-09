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
    max_result = box_list[0]
    min_result = box_list[0]
    for box_height in box_list:
        if box_height >= max_result:
            max_result = box_height
        if box_height <= min_result:
            min_result = box_height

    result = max_result - min_result
    print(f'#{tc} {result}')