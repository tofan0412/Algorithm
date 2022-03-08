from itertools import permutations, combinations

def check_order(s):
    correct = True
    for i in range(len(s)-1):
        if total_alphabet.index(s[i]) > total_alphabet.index(s[i+1]):
            correct = False
    return correct


# GOLD5
gather = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
total_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y,' 'z']

# permutations 쓰면 메모리 초과 발생한다..
# l은 암호의 길이, c는 후보 문자의 길이를 뜻한다.
l, c = map(int, input().split())
alphabets = list(map(str, input().split()))

# 전략) 1개의 모음, 2개의 자음을 선택하고 l - 3만큼 남는 자리에 남는 문자를 넣자.
cand_gather, cand_conso = [], []
for a in alphabets:
    if a in gather:
        cand_gather.append(a)
    else:
        cand_conso.append(a)

# 1. 모음 선택

answer = []
for gather in cand_gather:
    # 2. 자음 2개 선택
    consos = list(combinations(cand_conso, 2))

    for conso in consos:
        tmp = list(alphabets)
        result = [gather, conso[0], conso[1]] # 3개는 뽑았다.
        tmp.remove(gather)
        tmp.remove(conso[0])
        tmp.remove(conso[1])

        # 이제 tmp에서 자음, 모음 상관없이 l - 3개만큼 뽑으면 된다.
        candidates = list(combinations(tmp, l - 3))
        for cand in candidates:
            cand = list(cand)
            result_tmp = list(result)
            result_tmp = result_tmp + cand

            # 모두 뽑았으므로 이제 순서에 맞는 애들만 생각해보자.
            tmp = list(permutations(result_tmp, l))
            for case in tmp:
                is_correct = check_order(case)
                if is_correct:
                    if case not in answer:
                        answer.append(case)


for ans in answer:
    ans_str = ''
    for s in ans:
        ans_str += str(s)
    print(ans_str)

