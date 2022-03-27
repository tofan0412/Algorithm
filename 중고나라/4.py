'''
단어 퍼즐은 주어진 단어 조각을 이용해 주어진 문장을 완성하는 퍼즐이다.
이 때 주어진 각 단어는 무한개로 존재한다.

주어진 문장을 완성하기 위해 사용해야 하는 단어 조각 개수의 최소값을 return하도록 완성!
불가능한 경우 -1 return
'''
answer = []


def search(strs, word, cnt):
    global answer
    a = 3
    # 문자열을 완성했다면 cnt 반환
    if word == "":
        answer.append(sum(cnt))
        return

    cannot = True
    for i, keyword in enumerate(strs):
        # 해당 키워드가 만약 단어에 있다면
        if keyword in word:
            cannot = False

            idx = word.index(keyword)
            # 해당 단어를 제외하고, 단어 사용횟수를 카운트한다.
            new_word = word[:idx] + word[idx + len(keyword):]
            tmp = list(cnt)
            tmp[i] += 1
            # 다시 재귀로 진행한다.
            search(strs, new_word, tmp)
    # 모든 단어에 대해 더이상 제외할 수 없다면?
    if cannot:
        return


def solution(strs, t):  # t는 만들어야 하는 문자열, strs는 단어조각
    able = []

    search(strs, t, [0] * len(strs))

    return answer


solution(["ba", "an", "nan", "ban", "n"], "banana")
print(answer)
