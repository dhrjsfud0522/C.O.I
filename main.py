n, m = list(map(int, input().split()))
l = list(range(1, n + 1))
a = []
b = []

for _ in range(m):
    i, k, j = list(map(int, input().split()))
    a = l[k : j + 1]
    b = l[i : k]
    for q in range(0, len(b) - 1):
        l[i + q] = b[q]
    for w in range(0, len(a) - 1):
        l[k + w] = a[w]

print(*l)

