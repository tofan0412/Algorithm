def solution(goods):
    for good in goods:
        candidates = []

        # size에 대한 for문
        for size in range(1, len(good)):
            for i in range(len(good)):
                voca = good[i:i+size]




solution(["pencil","cilicon","contrabase","picturelist"])
solution(["abcdeabcd","cdabe","abce","bcdeab"])
