# 마이쮸 시뮬레이션 구현

N = 20
queue = [(1,0)] # 초기화

#(O,O) [0]: 사람번호, [1]: 직전까지 받았던 마이쮸의 개수

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0) # 받으러온 사람, 저번까지 받은 개수

    last_people = num # 마지막으로 받으러 온 사람
    cnt += 1 # 저번보다는 하나 더 챙겨 가자

    N -= cnt # num이라는 친구가 cnt 개수만큼 가져감
    new_people += 1

    queue.append((num, cnt)) # num이라는 사람이 cnt만큼 가져갔더라. 맨 뒤로 가서 다시 줄을 선다
    queue.append((new_people, 0)) # 처음 줄을 섰으므로, 0개만큼 마이쮸를 가져갔다.

print(last_people)