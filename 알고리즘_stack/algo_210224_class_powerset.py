# backtracking을 이용하여 부분집합 구하기

arr = [1,2,3,4,5,6,7,8,9,10]
N = len(arr)
select = [0]*N
def powerset(idx): # idx는 원소를 선택하기 위해 필요한 기준 인덱스를 의미한다.
    if idx == N:
        total = 0
        for i in range(N):
            total += arr[i]
            if total == 10:
                print(select)
        return
    # idx 자리의 원소를 뽑고 간다.
    select[idx] = 1 # True
    powerset(idx+1)

    # idx 자리의 원소를 뽑지 않고 간다.
    select[idx] = 0
    powerset(idx+1)

powerset(0)