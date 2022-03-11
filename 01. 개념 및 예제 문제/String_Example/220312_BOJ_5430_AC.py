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
    for func in p:
        if func == "R":
            # 배열을 뒤집는다.
            numbers.reverse() # 이 부분이 시간초과 발생
        elif func == "D":
            # 배열이 비어있는 경우, 에러를 출력한다.
            if len(numbers) == 0:
                print("error")
                ans = False
                break
            else:
                # 배열의 첫번째 값을 제거한다.
                numbers.pop(0)
    if ans:
        print(numbers)

