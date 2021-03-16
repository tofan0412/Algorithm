T = int(input())
# 최소 단위 시간을 구하는 것에 주목해야 한다.
#
for tc in range(1, T+1):
    N = int(input())
    # 이 때 N은 학생수이다.

    corrider = [0]*200 # 복도를 의미한다.

    # 학생 한 명 한명에 대해 출발지-도착지 정보를 받는다.
    point = [0]*N
    for i in range(N):
        s,e = list(map(int, input().split()))
        point[i] = [s//2-1 if not s%2 else s//2,e//2-1 if not e%2 else e//2]
        # 방 번호를 오름차순으로 변경한다.
        point[i].sort() # (0번 방에서 2번방으로 가나, 2번방에서 0번 방으로 가나 복도 점유 공간은 동일)

    # point 자체를 정렬을 해보자 # 이 부분을 하지 않으면 왜 에러가 발생하는가?
    point = sorted(point, key = lambda x : x[0])

    check = [False]*N
    # 이 때, point는 corrider를 점거할 시작 인덱스와 끝 인덱스를 의미한다.

    time = 0 #  단위시간을 카운트한다.
    while False in check: # 모든 학생이 방 이동을 끝낼때까지
        # 한번의 단위 시간이 끝났으므로 복도를 초기화 한다.
        corrider = [0] * 200
        for student in range(N):
            # 만약 이미 점거되어 있다면? 안된다.
            if 1 in corrider[point[student][0]:point[student][1]+1]:
                continue # 다음 학생을 고려한다.
            # 경로 간 1이 없다면?
            elif 1 not in corrider[point[student][0]:point[student][1]+1] and check[student] == False:
                p1 = point[student][0]
                p2 = point[student][1]+1

                for k in range(p1,p2):
                    corrider[k] = 1
                check[student] = True
        time += 1

    print(f'#{tc} {time}')




# Answer - 박동주
# T = int(input())
# for test_case in range(1,T+1):
#     # 400개 방 1 2 // 3 4 식으로
#     #복도의 구간이 겹치면 동시에 못들어간다
#     # 그리디 알고리즘으로 먼저 끝방정렬하고 앞방 정렬하면?
#     N = int(input())
#     arr = []
#     for i in range(N):
#         a,b = map(int,input().split())
#         if a>b:
#             a , b = b , a
#         arr.append([a,b])
#     #arr = sorted(arr,key = lambda x : x[1],reverse=True)
#     arr = sorted(arr,key=lambda x: x[0])
#     cnt = 0
#     while arr:
#         tmp = arr.pop(0)
#         cnt +=1
#         chk = arr[:]
#         for i in chk:
#             if i[0]>tmp[1]:
#                 if tmp[1]+1 == i[0] and i[0]%2==0:
#                     pass
#                 else :
#                     tmp = i
#                     arr.remove(i)
#             else:
#                 pass
#     print('#{} {}'.format(test_case,cnt))

