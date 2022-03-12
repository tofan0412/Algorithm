# GOLD5
T = int(input())
for tc in range(T):
    p = input() # 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    numbers = input()

    numbers = numbers.replace("[", "")
    numbers = numbers.replace("]", "")

    # 이렇게 처리했는데 만약 numbers가 ''가 나온다면?
    if numbers == '':
        print("error")
        continue
    else:
        numbers = list(map(int, numbers.split(",")))

    # 이제 각 함수를 수행하자.
    ans = True
    # 풀이) reverse를 아예 잊어버려야 한다.
