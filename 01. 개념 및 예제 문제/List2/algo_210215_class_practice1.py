# Practice 1
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for row in range(len(arr)):

    for col in range(len(arr[row])):
        sum = 0
        print(f'시작합니다. 현재위치 : ({row},{col})')

        # 1. 상
        nr_up = row + dr[0]
        nc_up = col + dc[0] # 변함 없다.
        # 해당하는 값이 유효한 인덱스 범위에 존재하는지를 계산해야 한다.
        if 0 <= nr_up < len(arr): # 범위 안에 있다.
            sum += abs(arr[row][col] - arr[nr_up][nc_up])
        else:
            print(f'현재 위치는 [{row}][{col}]이고 위값이 존재하지 않습니다.')

        # 2. 하
        nr_down = row + dr[1]
        nc_down = col + dc[1] # 변함없다.
        if 0 <= nr_down < len(arr):
            sum += abs(arr[row][col] - arr[nr_down][nc_down])
        else:
            print(f'현재 위치는 [{row}][{col}]이고 아래값이 존재하지 않습니다.')

        # 3. 좌
        nr_left = row + dr[2] # 고려할 필요가 없다.
        nc_left = col + dc[2]
        if 0 <= nc_left < len(arr[row]):
            sum += abs(arr[row][col] - arr[nr_left][nc_left])
        else:
            print(f'현재 위치는 [{row}][{col}]이고 왼쪽값이 존재하지 않습니다.')

        # 4. 우
        nr_right = row + dr[3]  # 고려할 필요가 없다.
        nc_right = col + dc[3]
        if 0 <= nc_right < len(arr[row]):
            sum += abs(arr[row][col] - arr[nr_right][nc_right])
        else:
            print(f'현재 위치는 [{row}][{col}]이고 오른쪽값이 존재하지 않습니다.')

        print(f'합은 {sum}입니다.')


# Practice 2
# 10개의 정수를 입력받아, 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를
# 작성해보자.
arr2 = [-2,1,9,3,4,-3,5,-6,8,2]