# 정수를 string으로 변환해보자.

# 1. 문자 뒤집기

s = "Reverse the strings"

arr = []
result = ""
# mutable한 list로 변환하기
for char in s:
    arr.append(char)

for char in range(len(arr)-1, -1,-1):
    result += arr[char]
print(result)

# 1-1. swap을 통해서도 구현할 수 있다.
for i in range(0,len(arr)//2):
    arr[i], arr[-1-i] = arr[-1-i], arr[i]
print(arr)

# 2. 양의 정수를 입력 받아, 문자열로 변환하기

# 한 자리 한자리 검사 받아야 한다.

number = 1234

result = ""
tmp = []
while number > 0:
    rest = number % 10 # 한자리가 된다.
    number = number // 10 # 몫을 number로 저장한다.
    ascii_val = 48 + rest
    tmp.insert(0, ascii_val)

for i in tmp:
    result += chr(i)

print(result, type(result))










