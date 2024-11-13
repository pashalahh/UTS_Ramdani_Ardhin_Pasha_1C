jumlah_barang = int(input('Masukan Jumlah Barang : '))
total = 0
for x in range (jumlah_barang):
    harga = int(input(f'Harga Barang Ke-{x+1} = '))
    total += harga

print(f'Total Belanjaan : Rp.{total}')