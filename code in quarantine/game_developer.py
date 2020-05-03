(d, h) = (int(x) for x in input().split())
if d > h:
    a, b = d, h
else:
    a, b = h, d
if a == 0 and b == 0:
    print(0)
if a > 0 and b == 0:
    print('NP')
elif a > 0 and b > 0:
    val = a//b
    pow2 = 0
    loli = 1
    while val > loli:
        loli *= 2
        pow2 += 1
    if val == loli:
        pow2 = pow2
    elif val < loli:
        pow2 -= 1
    if a == b:
        print(a)
    else:
        print(a+pow2+1)
