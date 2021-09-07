queue = [0]*3
# front와 rear를 설정한다.
front, rear = -1, -1
# 큐에 데이터를 넣는다.

def isFull(queue):
    factor = True
    for item in queue:
        # 0인게 하나라도 있으면 비어있지 않은 큐이다.
        if item == 0:
            factor = False
    return factor

def isEmpty(queue):
    global front
    global rear
    if front == rear:
        return True
    else: return False

def enQueue(queue, item):
    global rear
    # 큐가 가득 찼는지를 먼저 확인해야 한다.
    if not isFull(queue):
        rear += 1
        queue[rear] = item

def deQueue():
    global front
    # 큐가 비었는지, 비어있지 않은지를 확인한다.
    if not isEmpty(queue):
        front += 1
        return queue[front]

# 큐에 데이터 넣기
enQueue(queue, 1)
print(queue)
enQueue(queue, 2)
print(queue)
enQueue(queue, 3)
print(queue)
# 큐에서 데이터 추출하기
print(deQueue())
print(deQueue())
print(deQueue())




