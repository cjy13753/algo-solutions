import sys

# Merge sort

def mergesort(words: list) -> None:
    if len(words) > 1:
            
        partition_index = len(words) // 2
        L = words[:partition_index]
        R = words[partition_index:]
        
        mergesort(L)
        mergesort(R)

        i = 0
        p = 0
        q = 0
        
        while p < len(L) and q < len(R):
            if compare(L[p], R[q]):
                words[i] = R[q]
                q += 1
            else:
                words[i] = L[p]
                p += 1
            i += 1
        
        while p < len(L):
            words[i] = L[p]
            p += 1
            i += 1
        
        while q < len(R):
            words[i] = R[q]
            q += 1
            i += 1

def compare(l_word: str, right_word: str) -> bool:
    if (len(l_word) > len(right_word)):
        return True
    elif (len(l_word) == len(right_word)):
        a_ls = list(l_word)
        b_ls = list(right_word)
        for i in range(len(l_word)):
            if a_ls[i] < b_ls[i]:
                return False
            elif a_ls[i] > b_ls[i]:
                return True
        return True
    else:
        return False

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().split()[0])

mergesort(words)
prevword = ""
for word in words:
    if word != prevword:
        print(word)
        prevword = word