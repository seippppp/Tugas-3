A, B, C = map(int,input().split())
D = list(map(int, input().split()))
total_energi = 0

for _ in range(C):
    X, Y = map(int,input().split())
    energi_perkasus = sum(D[X-1:Y-1])
    total_energi += energi_perkasus

if total_energi <= B:
    print(f"EZ banget, energiku sisa {B - total_energi}!")
else:
    print(f"NT, kurang {total_energi - B} energi sih.")