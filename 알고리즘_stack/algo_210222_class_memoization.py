# 메모이제이션
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0,1] # fibo(0), fibo(1)일 때의 값을 미리 메모리에 저장한다.

print(fibo1(40))

# 만약 fibo1(5)가 들어갔다고 가정하자.
# 이 때, memo는 [0,1]이다.
# fibo(4) + fibo(3)을 memo 리스트에 추가하게 된다.
# fibo(4)의 경우, n은 2보다 크고, 리스트의 크기는 ?이다.
# fibo(3)의 경우 n은 3보다 크고, 리스트의 크기는 ?이다.
# fibo(2)의 경우 n은 2보다 크거나 같고, 리스트의 크기는 2로, 같다.

###########################################

memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1: # 값을 구해야 한다.
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n] # 값이 기록되어 있는 경우에는, 해당 값을 반환한다!

print(fibo2(10))
print(memo2)
