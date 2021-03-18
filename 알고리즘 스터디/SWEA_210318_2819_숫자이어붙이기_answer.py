def max_money(index, number):
    global result
    # 0번째 인덱스부터 시작한다.
    change1 = change # change1은 변경 횟수이다.
    # 인덱스가 주어진 리스트의 길이와 같아지거나, 변경횟수와 동일한 경우
    if index == len(number) - 1 or index == change1:

        while index < change1:
            number[-1], number[-2] = number[-2], number[-1]
            change1 -= 1

        number3 = int(''.join(number))
        if result < number3:
            result = number3
        return

    # 배열의 0번째 element부터 마지막 element까지 모두 확인한다.
    for i in range(index, len(number)):
        for j in range(i + 1, len(number)):
            # selection sort와 유사하다.
            # 0 ~ 마지막까지 중에서 최대값을 찾아 0번째에 배치하고
            # 1 ~ 마지막까지 중에서 최대값을 찾아 1번째에 배치하고
            # ...
            # n ~ 마지막까지 중에서 최대값을 찾아 마지막에 배치한다.
            number2 = list(number) # number는 원본배열이고, number2는 deep copy한 복사본이다.
            # swap한다.
            number[i], number[j] = number[j], number[i]
            print(number)
            max_money(index + 1, number)
            number = list(number2) # 원복한다.


T = int(input())

for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    num, change = input().split() # num은 숫자 배열을, change는 변경 횟수를 의미한다.
    change = int(change) # 정수로 변환하기
    number = []

    # 받은 숫자 배열을 리스트로 변환하기 / 123 -> [1,2,3]
    for i in num:
        number.append(i)

    result = 0

    max_money(0, number)

    print(result)