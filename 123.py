a = []
for i in range(42, 101, 2):
    c = 0
    while i % 2 == 0:
        i //= 2
        c += 1
    a.append(c)
c = 0
for i in a:
    c += i

