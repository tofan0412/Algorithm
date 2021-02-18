# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# 이 때, 정사각형 모양의 파리채를 이용해 최대한 많은 파리를 죽이고자 한다.

T = int(input())

for tc in range(1, T+1):
    N,M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for i in range(N)]

    sum_list = []
    # 정사각형의 왼쪽 위 모서리를 기준으로 잡자. 이 때 range는 n-m+1을 활용하자.
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0 # 꼭지점 (i,j)를 기준으로 M 길이만큼의 정사각형 내의 값을 모두 더해야 한다.
            for row in range(i, i+M):
                for col in range(j,j+M):
                    sum += arr[row][col]
            sum_list.append(sum)

    print(f'#{tc} {max(sum_list)}')
