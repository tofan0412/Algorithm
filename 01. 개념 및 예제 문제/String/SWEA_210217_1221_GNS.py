T = int(input())
for tc in range(1, T+1):
    zero = [];one = [];two = []
    three = [];four = [];five = []
    six = [];seven = [];eight = [];nine = []
    result = ""

    tc_info = list(input().split())
    tc_num = tc_info[0] # 번호
    tc_length = int(tc_info[1]) # 개수

    case = input().split()

    for num in case:
        if num == "ZRO":
            zero.append("ZRO")
        elif num == "ONE":
            one.append("ONE")
        elif num == "TWO":
            two.append("TWO")
        elif num == "THR":
            three.append("THR")
        elif num == "FOR":
            four.append("FOR")
        elif num == "FIV":
            five.append("FIV")
        elif num == "SIX":
            six.append("SIX")
        elif num == "SVN":
            seven.append("SVN")
        elif num == "EGT":
            eight.append("EGT")
        else:
            nine.append("NIN")

    result += " ".join(zero) + " "
    result += " ".join(one) + " "
    result += " ".join(two) + " "
    result += " ".join(three) + " "
    result += " ".join(four) + " "
    result += " ".join(five) + " "
    result += " ".join(six) + " "
    result += " ".join(seven) + " "
    result += " ".join(eight) + " "
    result += " ".join(nine) + " "
    print(f'{tc_num}')
    print(f'{result}')
