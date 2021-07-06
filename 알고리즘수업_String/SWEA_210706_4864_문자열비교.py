# T = int(input())
#
# for tc in range(1, T+1):
#     str1 = input() # 길이가 N인 문자열
#     str2 = input() # 길이가 M인 문자열
#     p1 = 0
#     p2 = 0
#     result = 0
#
#     while True:
#         # P1의 포인터가 len()인 경우, str2에 str1이 포함되어 있다는 뜻이다.
#         if p1 == len(str1):
#             result = 1
#             break
#         elif p2 == len(str2):
#             break
#
#         # 한 글자가 일치하면, str1과 str2 모두 포인터를 1 증가
#         if str1[p1] == str2[p2]:
#             p1 += 1
#             p2 += 1
#         # 일치하지 않으면, p1의 포인터는 다시 0으로, p2의 포인터는 1증가
#         else:
#             p1 = 0
#             p2 += 1
#
#     print(f"#{tc} {result}")


# for문으로 다시 짜보자.
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    p1 = 0
    result = 0

    for j in range(len(str2)):
        # 일치하는 경우 : str1과 str2 문자 모두 다음 포인터로 이동.
        if str1[p1] == str2[j]:
            p1 += 1
            # 만약 p1의 포인터가 str1의 길이를 넘어가는 경우: IndexError가 발생할 수 있으므로 처리해둔다.
            if p1 == len(str1):
                result = 1
                break
            continue
        # 일치하지 않는 경우
        else:
            # str1의 포인터 초기화
            p1 = 0
            continue

    print(f'#{tc} {result}')



