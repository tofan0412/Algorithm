N = 3
arr = [1,2,3]

sel = [0] * N # a 리스트 ( 내가 해당 원소를 뽑았는지 체크하는 리스트이다. )
# 만약 sel = [1,0,1] 이면 arr의 1, 3을 원소로 선택했다는 뜻이다.

def powerset(idx): # idx는 원소를 선택하기 위해 필요한 기준 인덱스를 의미한다.
    if idx == N:
        print(sel, ":", end=" ")
        for i in range(N):
            if sel[i]:
                print(arr[i],end=' ')
        print()
        return
    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1 # True
    powerset(idx+1)

    # idx 자리의 원소를 뽑지 않고 간다.
    sel[idx] = 0
    powerset(idx+1)

powerset(0)