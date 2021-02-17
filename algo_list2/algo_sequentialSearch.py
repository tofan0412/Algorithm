# 배열이 정렬되어 있지 않은 경우
arr = [4,9,11,23,19,7]

key = 11

for i in range(len(arr)):
    if key == arr[i]:
        print(f"{i}에 위치하고 있습니다.")
        break # 더 이상의 진행은 필요없다.
else: # for문이 모두 수행된 이후 실행된다.
    print("찾지 못했습니다.")

# 배열이 정렬되어 있는 경우
arr = [4,7,9,11,19,23]

for i in range(len(arr)):
    if key == arr[i]:
        print(f'{i}에 위치하고 있습니다. ')
        break
    elif key < arr[i]:
        print(f'{i}번째까지만 탐색해봄..')
        break
else:
    print("찾지 못했습니다.")