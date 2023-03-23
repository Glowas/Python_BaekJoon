n, m = map(int, input().split(' '))
li = [i for i in range(1, n+1)]

for t in range(m):
    i, j = map(int, input().split(' '))
    z = 0
    while(True):
        z += 1
        li[i-1] = li[j-z]
        swap = li[i-1]
        li[j-z] = swap
        if i >= j-z:
            break
        i += 1
print(*li)
