berat = int(input('Masukan Berat Badan (Kg) : '))
tinggi = float(input('Masukan Tinggi Badan (M) : '))
print(f'Berat Badan : {berat}')
print(f'Tinggi Badan : {tinggi}')
BMI = berat / (tinggi*tinggi)
print(f'Nilai BMI Anda : {BMI}')
if BMI < 18.5 :
    print('Kategori BMI : Berat badan kurang')
elif 18.5 <= BMI < 24.9 :
    print('Kategori BMI : Berat badan ')
elif 25 <= BMI < 29.9 :
    print('Kategori BMI : Kelebihan berat badan')
else:
    print('Kategori BMI : Obesitas')