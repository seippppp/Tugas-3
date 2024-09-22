x1, y1 = map(int,input().split())
xs, ys = map(int,input().split())
xf, yf = map(int,input().split())

#jarak antara raja dengan warga
king_warga = (((xf - xs)**2) + ((yf - ys)**2))**0.5

#jarak antara raja dengan virus
king_bug = (((xf - x1)**2) + ((yf - y1)**2))**0.5

if king_bug > king_warga:
    print("Yes")
else:
    print("No")