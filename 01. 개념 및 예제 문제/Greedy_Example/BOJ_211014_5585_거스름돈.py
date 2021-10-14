'''
잡화점에는 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있다.
또한 잡화점에선 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
'''

payment = int(input())  # 타로가 지불한 돈이다.
rest = 1000 - payment

# 그리디 알고리즘은 매 순간순간 최선의 선택을 하는 것.
sort = [500, 100, 50, 10, 5, 1]

result = 0
for kind in sort:
    count = rest // kind
    result += count
    rest -= kind * count

print(result)