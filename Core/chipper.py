# Import module abjad yang telah dibuat sebelumnya

import __init__
from abjad import abjad1, abjad2

# Fungsi untuk mengambil Input User yang ingin dijadikan plain text

def InputUser(user):
	text = user
	return text.lower()

# Fungsi untuk menerima kunci dari user yang ingin digunakan

def KunciUser(kunci):
	return kunci

# Fungsi Untuk Mengkripsi text

def Encrypt(text, Kunci):
	# Tahap Pertama : Mengubah huruf menjadi angka
	awal1 = 0 # Untuk Tahap Pertama
	akhir1 = 1 # Untuk Tahap Pertama

	awal2 = 0 # Untuk Tahap Kedua

	awal3 = 0
	
	HurufAngka = [] # Untuk Tahap Pertama
	Pengacakan = [] # Untuk Tahap Kedua
	HurufAcak = [] # Untuk Tahap Ketiga

	for i in range(len(text)): # Iterasi nilai str

		huruf = text[awal1:akhir1]
		awal1 += 1
		akhir1 += 1

		HurufAngka.append(abjad1.get(huruf)) # Mengubah string menjadi angka dan memasukkan nya ke list HurufAngka



	# Tahap Kedua : Mengacak angka agar tidak bisa dibaca orang lain

	for i in range(len(HurufAngka)):

		Acak = (HurufAngka[awal2] + Kunci) % 26
		awal2 += 1

		Pengacakan.append(Acak)

	

	# Tahap ketiga : Mengubah Angka menjadi huruf acak

	for i in range(len(Pengacakan)):
		AcakHuruf = Pengacakan[awal3]
		awal3 += 1

		HurufAcak.append(abjad2.get(AcakHuruf))

	return HurufAcak

# Untuk Mengubah huruf acak kembali menjadi huruf normal

def Decrypt(text, Kunci):
	awal = 0

	AngkaDecrypt = []
	HasilDecrypt = ''

	for i in range(len(text)):
		number = text[awal]
		awal += 1

		AngkaDecrypt.append(abjad1.get(number))

	for i in AngkaDecrypt:

		decr = i - Kunci

		if decr < 0:
			decr += 26
			decr %= 26
		elif decr == 26:
			decr += 26
			decr %= 26
		else:
			decr += 26
			decr %= 26

		HasilDecrypt += abjad2.get(decr)

	return HasilDecrypt