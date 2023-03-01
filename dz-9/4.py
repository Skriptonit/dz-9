a = [int(i) for i in input().split()]
n = set()
for i in a:
    if i in n :
        print("YES")
    else :
        print('NO')
    n.add(i)
