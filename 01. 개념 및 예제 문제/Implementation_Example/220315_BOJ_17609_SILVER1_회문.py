# SILVER1
tc = int(input())
cases = []
for _ in range(tc):
    cases.append(list(input()))

for case in cases:
    is_palindrome = True
    is_half_palindrome = False

    p1 = 0
    p2 = len(case) - 1




