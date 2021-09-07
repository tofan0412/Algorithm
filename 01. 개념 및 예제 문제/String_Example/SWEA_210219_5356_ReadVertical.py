# 의석이의 세로로 말해요
T = int(input())

for tc in range(1, T+1):

    arr = [list(input()) for i in range(5)]
    result = ""
    length = [len(arr[i]) for i in range(len(arr))]
    max_length = 0

    # 입력을 받으면서, max를 갱신할 수도 있다.
    # for i in range(5):
    #     word[i] = list(input())
    #
    #     if len(word[i]) > max_length:
    #         max_length = len(word[i])

    for size in length:
        if max_length < size:
            max_length = size

    # 가장 긴 단어를 기준으로 열 우선 탐색을 진행해야 한다.
    for j in range(max_length): # column
        for i in range(len(arr)): # row
            if len(arr[i]) > j: # 해당열에 해당하는 문자가 존재한다는 것을 의미한다.
                result += arr[i][j]
            else:
                pass

    print(f'#{tc} {result}')

# try-except를 쓰면 굳이 위와 같이 작성하지 않아도 된다.

# try:
#     print(word[j][i], end="")
# except:
#     pass # 별도로 처리할 건 없다.