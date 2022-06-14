'''
길이가 N인 정수 배열 A와 B가 있다. 함수 S는 다음과 같이 정의된다.
S = A[0] x B[0] + ... + A[N-1] x B[N-1]
이 때 S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열해선 안된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.

ex)
1 1 1 6 0
2 7 8 3 1
정렬해보자.
B : 8 7 3 2 1
A : 0 1 1 1 6
0 + 7 + 3 + 2 + 6 = 18

'''

N = int(input())
A = map(int, input().split())
B = map(int, input().split())
# 이 때 B의 순서는 고정이다.
B = sorted(B)
B.reverse()
A = sorted(A)

result = 0
for i in range(N):
    result += A[i]*B[i]

print(result)




