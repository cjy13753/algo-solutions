import sys

# Quick sort
def quicksort(words):
    quicksort_core(words, 0 ,len(words) - 1)

def quicksort_core(words: list, start: int, end: int) -> None:
    if len(words[start:end + 1]) <= 1:
        return
    if start > end:
        return
    
    p = partition(words, start, end)
    quicksort_core(words, start, p - 1)
    quicksort_core(words, p + 1, end)

def partition(words: list, start: int, end: int) -> int:
    j = start
    p = start
    r = end

    while j < r:
        if compare(words[r], words[j]):
            swap(words, p, j)
            p += 1
        j += 1
    
    swap(words, p, r)

    return p

def compare(a: str, b: str) -> bool:
    if (len(a) > len(b)):
        return True
    elif (len(a) == len(b)):
        a_ls = list(a)
        b_ls = list(b)
        for i in range(len(a)):
            if a_ls[i] < b_ls[i]:
                return False
        return True
    else:
        return False

def swap(words: list, a: int, b: int) -> None:
    tmp = words[a]
    words[a] = words[b]
    words[b] = tmp

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().split()[0])

quicksort(words)
prevword = ""
for word in words:
    if word != prevword:
        print(word)
        prevword = word