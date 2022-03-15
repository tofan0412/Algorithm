class CircularQueue:

    def __init__(self, n):
        self.MAXSIZE = n
        self.front, self.rear = -1, -1
        self.cnt = 0 # 현재 큐에 들어가 있는 데이터 수. MAXSIZE를 넘을 수 없다.
        self.queue = [0 for _ in range(self.MAXSIZE)]

    # 현재 들어가 있는 데이터 수를 반환
    def getSize(self):
        return self.cnt

    # 현재 원형 큐가 비어있는지 확인
    def isEmpty(self):
        return self.cnt == 0

    # 현재 원형 큐가 모두 찼는지 확인
    def isFull(self):
        return self.cnt == self.MAXSIZE

    # 데이터 넣기
    def enqueue(self, data):
        # 데이터를 넣기 전에 데이터가 모두 찼는지 확인해야 한다.
        if self.isFull():
            raise IndexError("Queue is Full")

        # 1. 데이터를 넣어야 하므로 rear +1
        self.rear = (self.rear + 1) % self.MAXSIZE
        self.queue[self.rear] = data
        self.cnt += 1

    # 데이터 빼기
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")

        self.front = (self.front + 1) % self.MAXSIZE
        data = self.queue[self.front]
        self.cnt -= 1
        return data

    # 가장 앞의 데이터 반환하기
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue[self.front + 1] % self.MAXSIZE


if __name__ == '__main__':
    queue = CircularQueue(4)
    print("queue = " + str(queue.queue))
    print("isEmpty = " + str(queue.isEmpty()))
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("isFull = " + str(queue.isFull()))

    print("peek = " + str(queue.peek()))
    queue.dequeue()
    queue.dequeue()
    print("peek = " + str(queue.peek()))
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
