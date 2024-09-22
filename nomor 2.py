import numpy as np
total_input = int(input("masukkan berapa jumlah inputan: "))
arr_numbers = [0] * total_input

for i in range(total_input):
    numbers = int(input("masukkan angka: "))
    arr_numbers[i] = numbers

final_result = ""
for numbers in arr_numbers:
  # convert inputan ke biner
  binary = np.binary_repr(numbers, width=32)

  # bagi bilangan biner menjadi 8 bit
  splitted_binary = [str(binary)[i:i+8] for i in range(0, len(str(binary)), 8)]

  result = ""
  for i in splitted_binary:
    # convert bilangan biner yang sudah dibagi menjadi desimal
    decimal = int(i, 2)

    # convert desimal ke karakter ASCII
    result += chr(decimal)
  final_result += result

print(final_result)