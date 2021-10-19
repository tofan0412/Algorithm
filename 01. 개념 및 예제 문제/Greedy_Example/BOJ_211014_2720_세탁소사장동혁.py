'''
리암이 자꾸 0.5달러를 5달러로 줌..
'''
import decimal

sort = [0.25, 0.1, 0.05, 0.01]

tc = int(input())
for i in range(tc):
    result = [0] * len(sort) # 결과값 초기화
    C = int(input())# 거스름돈
    C = C / 100 # 달러 단위로 바꾸기

    for (index, kind) in enumerate(sort):
        # 거스를 수 있는 단위인지 확인
        if C >= kind:
            count = C // kind
            result[index] = int(count)
            C -= float(decimal.Decimal(count * kind))
        else:
            continue

    print(f'{result[0]} {result[1]} {result[2]} {result[3]}')




