# GOLD5
gather = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"
l, c = map(int, input().split())
alphabets = list(input().split())

# 1. alphabets 정렬 -> 증가하는 순서로 맞추기 위해
alphabets.sort()
# 2. l개를 선택할지 안할지
result = []


def solution(choice, i):
    global result
    # 만약 l개의 문자를 모두 선택했다면 후보군에 집어넣는다. or 아예 선택안한 경우..
    if len(choice) == l:
        result_str = ''
        cnt_gather, cnt_consonant = 0, 0

        for s in choice:
            # 모음, 자음 개수를 센다.
            if s in gather:
                cnt_gather += 1
            elif s in consonant:
                cnt_consonant += 1
            result_str += str(s)

        # 1개의 모음, 2개의 자음 이상 & 새로운 케이스인 경우 추가
        if cnt_gather > 0 and cnt_consonant > 1:
            result.append(result_str)
        return

    if i == len(alphabets):
        return

    # 현재 인덱스 포함시키기
    tmp = list(choice)
    tmp2 = list(choice)
    tmp.append(alphabets[i])
    solution(tmp, i+1)
    solution(tmp2, i+1)


solution([], 0)
for ans in result:
    print(ans)
