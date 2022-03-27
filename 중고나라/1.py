# 한 버튼에 적힌 문자를 연속으로 입력하고 싶을 때는, 버튼의 입력 사이에 0을 입력해야 한다.
# 0은 오로지 한 버튼에 적힌 문자를 연속으로 입력하고 싶을 때만 눌렀다
# 같은 숫자는 최대 연속으로 3개까지만 나타난다.
def solution(s):
    # 숫자번호에 맞추기위해 0번째에 더미를
    # 마지막 숫자까지 카운트하기 위해 E추가
    # cnt에 맞추기 위해 X 추가
    keypad = ['DUMMY', 'X.QZ', 'XABC', 'XDEF', 'XGHI', 'XJKL', 'XMNO', 'XPRS', 'XTUV', 'XWXY']

    last_num = s[0]
    cnt = 1
    ans = ''

    s += 'E'

    for num in s[1:]:
        # 1. 같은 문자인 경우 cnt만 늘린다.
        if last_num == num:
            cnt += 1
        # 2. 0이 아닌 다른 문자인 경우, 세어진 cnt를 기준으로 문자를 붙인다.
        if num != '0' and last_num != num: # 마지막 순서인 E일 때도 수행된다.
            ans += keypad[int(last_num)][cnt]
            # last_num과 cnt 초기화
            last_num = num
            cnt = 1
        # 3. 만약 0이 입력되었다면, last_num은 유지되고 cnt만 0으로 변경된다.
        # 또한 현재문자 출력
        if num == '0':
            ans += keypad[int(last_num)][cnt]
            cnt = 0
    return ans