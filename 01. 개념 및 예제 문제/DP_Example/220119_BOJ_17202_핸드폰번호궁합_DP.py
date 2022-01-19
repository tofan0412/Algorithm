# BRONZE1
def solution(arr):
    a = 3
    if len(arr) == 2:
        print(f'{arr[0]}{arr[1]}')
        return arr

    fn = []
    for i in range(len(arr)-1):
        fn.append((arr[i] + arr[i+1]) % 10)
    return solution(fn)


A = list(map(int, list(input())))
B = list(map(int, list(input())))


# 합치자.
merged = []
for i in range(len(A)):
    merged.append(A[i])
    merged.append(B[i])

solution(merged)
