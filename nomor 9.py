masuk = input()
masuk = masuk.split()
x = int(masuk[0])
y = masuk[1]

if y == "aku":
    for i in range(1, x + 1):
        baris =[]
        for j in range(1,i+1):
            if (i + j) % 2 == 0:
                baris.append("I") #append itu buat menambahkan data ke akhir array
            else:
                baris.append("U")
        print(" ".join(baris))
elif y == "kamu":
    for i in range(1, x + 1):
        spasi = "  " * (x-i)
        baris =[]
        for j in range(1,i+1):
            if (i + j) % 2 == 0:
                baris.append("I")
            else:
                baris.append("U")
        print(spasi +" ".join(baris))