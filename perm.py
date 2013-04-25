def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i+1]
        if n==1:
            yield v
        else:
            rest = items[:i]+items[i+1:]
            for p in perm(rest, n-1):
                yield v+p

a = perm('abc')
for b in a:
    print b
    break
print '-'*20
for b in a:
    print b
