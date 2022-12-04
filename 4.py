import math as Math

def minAbsDiffPairs(arr):
    ans = []
    n = len(arr)

    arr.sort()

    minDiff = 10 ** 9

    for i in range(n - 1):
        minDiff = min(minDiff, Math.fabs(arr[i] -
                                         arr[i + 1]))

    for i in range(n - 1):
        pair = []
        if (Math.fabs(arr[i] - arr[i + 1]) == minDiff):
            pair.append(min(arr[i], arr[i + 1]))
            pair.append(max(arr[i], arr[i + 1]))
            ans.append(pair)

    return ans

arr = [4, 2, 1, 3]
N = len(arr)

pairs = minAbsDiffPairs(arr)

for v in pairs:
    print(f"{v[0]} {v[1]}")
