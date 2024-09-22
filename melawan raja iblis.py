U = int(input())
K = int(input())
M = int(input())

M_beku = M//2
K_beku = K//2

Gate1 = U - M_beku*2
Gate2 = Gate1 - K_beku*5*5
Gate3 = Gate2 - 1000

if Gate3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {Gate3}")
else:
    print("Yah! Ucup Meninggoy.")