from itertools import permutations
# GOLD5
gather = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# permutations 쓰면 메모리 초과 발생한다..
# l은 암호의 길이, c는 후보 문자의 길이를 뜻한다.
def solution(i, choice):
    global alphabets, result
    a = 3
    # 범위를 초과한 경우 종료
    if i == len(alphabets):
        return

    # 선택한 원소의 개수가 l개인 경우
    if len(choice) == l:
        if choice not in result:
            result.append(list(choice))
        return

    choice = list(choice) # DeepCopy
    # alphabets 리스트의 i번째 원소를 선택하자.
    choice.append(alphabets[i])
    solution(i+1, choice)
    # 선택하지 말자.
    choice.pop()
    solution(i+1, choice)


l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

alphabets.sort() # 알파벳 순서를 처음부터 맞춰두자.

# 이제 이 순서에 맞춰서 뽑으면 된다.
result = []
for i in range(len(alphabets)):
    solution(1, [])

print(result)
