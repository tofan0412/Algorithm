class Friend:
    def __init__(self, email):
        self.email = email
        self.friends = []

    # 각 객체의 friends라고 하는 리스트에 해당 친구의 객체를 추가한다. 
    def add_friendship(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def can_be_connected(self, friend):
        # 1. Direct로 연결되어 있는 경우
        if friend in self.friends:
            return True

        # 재귀적 풀이
        result = False
        for other_friends in self.friends:
            if result:
                break
            result = other_friends.can_be_connected(friend)
        return result


if __name__ == "__main__":
    a = Friend("A")
    b = Friend("B")
    c = Friend("C")

    a.add_friendship(b)
    b.add_friendship(c)

    print(a.can_be_connected(c))
