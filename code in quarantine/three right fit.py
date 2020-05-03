n = int(input())
a = input()
b = a.split()[:n]
c = list(map(int, b))
d = sorted(c)
for i in d:
    print(i, end=" ")
x = max(c)
y = min(c)
print()
print(x)
print(y)
print(x-y)
