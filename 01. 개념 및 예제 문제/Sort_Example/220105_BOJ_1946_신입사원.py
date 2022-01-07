# SILVER1
T = int(input())
for tc in range(T):
    N = int(input())
    grades = []
    for i in range(N):
        s_grade, i_grade = map(int, input().split())
        grades.append([s_grade, i_grade])

    # 1. 서류 성적 순으로 정렬 한다.
    grades = sorted(grades, key=lambda x:x[0])

    # 2. 뒤에서부터 내 앞사람들 중 최고 면접 성적과 내 면접 성적을 비교해서, 만약 내가 낮은 등수라면 나는 탈락
    min_order = len(grades)
    count = len(grades)
    for me in grades:
        if me[1] < min_order:
            min_order = me[1]

        if min_order < me[1]:
            count -= 1
    print(count)




