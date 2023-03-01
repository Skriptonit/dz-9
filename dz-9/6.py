n = int(input())
k = []
for i in range(n):
    for elem in input().split():
        k.append(elem)

print(len(set(k)))
