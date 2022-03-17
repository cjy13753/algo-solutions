def solution(numbers):
    ans = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            ans.add(numbers[i] + numbers[j])
    ans = list(ans)
    ans.sort()
    return ans