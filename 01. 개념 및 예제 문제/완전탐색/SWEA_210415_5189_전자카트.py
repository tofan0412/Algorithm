def perm(idx): # 0번 인덱스와 마지막 인덱스는 1로 고정이다.
    global ways
    if idx == len(section_list)-1: # 모든 원소에 대해 선택했다는 뜻이다. 시작, 마지막은 고려할 필요가 없다.
        # 이 중에서, 양 끝이 1인 대상만 저장한다.
        # ways.append(list(sel))
        result = 0
        for j in range(len(sel)-1):
            result += battery_map[sel[j]-1][sel[j+1]-1]
        values.append(result)
    else:
        for i in range(1, len(sel)-1): # 시작, 마지막은 고려 안해도 된다.
            if visited[i] == 0: # 아직 해당 원소를 선택하지 않았다면
                sel[idx] = section_list[i]
                visited[i] = 1 # 이미 사용했다는 뜻이다.
                perm(idx+1)
                visited[i] = 0
                sel[idx] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery_map = [list(map(int, input().split())) for _ in range(N)]

    section_list = [i for i in range(1, N+1)]
    section_list.append(1)
    # 이제 section_list에 대해 가능한 모든 순열을 구한다.
    visited = [0]*len(section_list) # 해당 원소의 방문 여부
    sel = [0]*len(section_list) # 해당 원소를 넣을 곳..
    sel[0], sel[-1] = 1, 1
    visited[0], visited[-1] = 1, 1
    values = []

    perm(1) # 1번째 인덱스부터 시작한다. 시작점은 이미 1로 되어 있으므로 할 필요가 없다.
    # 계산한 모든 가능한 경로에 대해, 배터리 소모량을 계산한다.
    print(f'#{tc} {min(values)}')
