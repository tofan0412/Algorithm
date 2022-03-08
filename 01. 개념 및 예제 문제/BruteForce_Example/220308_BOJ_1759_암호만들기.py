from itertools import permutations
# GOLD5
gather = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
total_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y,' 'z']

# c는 사용했을 법한 문자의 종류, l은 암호의 길이를 뜻한다.
l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

# 1. c개의 문자 중에서 l개의 문자를 뽑는 모든 경우의 수
candidates = list(permutations(alphabets, l))

tmp = []
# 2. 각 요소에 대해 1개의 모음, 2개의 자음을 포함하고 있는지 검사
for cand in candidates:
    # cand는 튜플이다.
    num_gather = 0
    num_consonant = 0
    for alpha in cand:
        if alpha in gather:
            num_gather += 1
        elif alpha in consonant:
            num_consonant += 1

    if num_gather > 0 and num_consonant > 1:
        tmp.append(cand)


result = []
for cand in tmp:
    is_candidate = True
    for i in range(len(cand)-1):
        if total_alphabet.index(cand[i]) > total_alphabet.index(cand[i+1]):
            is_candidate = False

    if is_candidate:
        result.append(cand)

for i in result:
    result_str = ''
    for j in i:
        result_str += str(j)
    print(result_str)




