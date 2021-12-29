prices = [4,5,6,7,8]
k = 2

result = []
n = len(prices)

def dfs(idx, tmp):
    if len(tmp) == k:
        result.append(tmp[:])
        return

    for i in range(idx, n):
        dfs(i+1, tmp + [prices[i]])

dfs(0, [])
print(result)