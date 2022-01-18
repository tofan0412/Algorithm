# n번째 피보나치 배열의 수를 출력하는 함수이다.
def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)

print(fibo(4))
