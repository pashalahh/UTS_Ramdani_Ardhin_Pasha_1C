tahun = int(input('Masukan Tahun : '))
if (tahun / 4 == 0 and tahun / 100 != 0):
    print(f"{tahun}Merupakan Tahun Kabisat")
else :
    print(f"{tahun} Bukan Tahun Kabisat")