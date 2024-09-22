a, b = map(int,input().split())
c = max(a,b)
d = min(a,b)

x = (c * d // a) + (c * d // b)
print(int(x))