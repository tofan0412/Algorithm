# SILVER1
T = int(input())
for tc in range(T):
    N = int(input())
    grades = []
    for i in range(N):
        s_grade, i_grade = map(int, input().split())
        grades.append([s_grade, i_grade])

    for (i, me) in enumerate(grades):
        for (j, you) in enumerate(grades):
            if me == you:
                continue
            if me[0] < you[0] and me[1] < you[1]:
                grades.pop(j)

            if you[0] < me[0] and you[1] < me[1]:
                grades.pop(i)
                break
    print(len(grades))