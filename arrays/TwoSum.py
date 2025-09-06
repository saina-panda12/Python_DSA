def twoSum(arr, target, n):
    freq = {}
    res = []

    # Build frequency map
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        complement = target - num
        if freq.get(num, 0) > 0 and freq.get(complement, 0) > 0:
            if num == complement and freq[num] < 2:
                continue  # need at least 2 of the same number

            # Store pair
            res.append((num, complement))

            # Decrement usage
            freq[num] -= 1
            freq[complement] -= 1

    if not res:
        return [(-1, -1)]
    return res


def takeInput():
    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr


def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print(f"{i[0]} {i[1]}")
        else:
            print(f"{i[1]} {i[0]}")


# -----------------------------
# Main driver code
# -----------------------------
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n, target, arr = takeInput()
        ans = twoSum(arr, target, n)
        printAns(ans)
