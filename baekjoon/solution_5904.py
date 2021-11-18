# n은 zero-indexed 기준
def recur(k: int, len: int, n: int):
    if k == 0:
        return 'moo'[n]
    prevLen = (len - (k + 3)) // 2
    if n <= prevLen - 1:
        return recur(k - 1, prevLen, n)
    elif n == prevLen:
        return 'm'
    elif n <= prevLen + (k + 3) - 1:
        return 'o'
    else:
        return recur(k - 1, prevLen, n - (prevLen + k + 3))

n = int(input()) - 1

k = 0
len = 3
while len < n + 1:
    k += 1
    len = 2 * len + k + 3
print(recur(k, len, n))