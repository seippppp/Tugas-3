import math

n = int(input())

nums = [int(input()) for _ in range(n)]

for q in nums:
    found = False
    limit = int(math.isqrt(q)) + 1

    for a in range(0, limit):
        if found:
            break
        for b in range(a, limit):
            if found:
                break
            for c in range(b, limit):
                if found:
                    break
                for d in range(c, limit):
                    if a * a + b * b + c * c + d * d == q:
                        found = True
                        break

    if found:
        print("LEAVE")
    else:
        print("ERASE")
