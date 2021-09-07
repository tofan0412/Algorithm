N = 20 # 마이쮸의 개수는 20개이다.
visited_cnt = [0]*10 # 사람이 줄을 설 때, 함께 추가한다.
queue = []

def myChew(number):
    global N # 남은 마이쮸의 개수를 의미한다.
    if N <= 0:
        return

    # 최초 방문인 경우
    if visited_cnt[number] == 0:
        queue.append(number) # 줄을 선다.
        tmp = queue.pop(0)
        visited_cnt[tmp] += 1
        N -= visited_cnt[tmp] # 남은 마이쮸의 개수를 수정한다.
        myChew(tmp) # 다시 줄을 선다.
    # 최초 방문이 아닌 경우
    else:
        queue.append(number) # 줄을 선다.
        visited_cnt[number] += 1
        myChew(number + visited_cnt[number]) # 내 다음 번호 사람을 뒤에 배치한다.
while N > 0:
    myChew(1)
