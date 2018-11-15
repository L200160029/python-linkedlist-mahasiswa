#! aplikasi data siswa sederhana menggunakan linked list python
#! create by alvin meko | 672010193 | fti-uksw
import os
import sys

pilih = 0
dataSiswa = []

def menu():
	os.system('cls')
	print("Menu Aplikasi Data Siswa LinkedList python");
	print("-------------------------------------------")
	print("1. Input Data Siswa")
	print("2. Tampilkan Data Siswa")
	print("3. Update Data Siswa")
	print("4. Hapus Data Siswa")
	print("5. Author")
	print("6. Keluar Aplikasi")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	elif pilih == 2:
		os.system('cls')
		print("TAMPIL DATA MAHASISWA ")
		baris = 1;
		for data in dataSiswa:
			print("Data ke ", baris)
			print("Nama : "+data[0])
			print("Nim  : "+str(data[1]))
			print("--------------------------")
			baris = baris+1
		raw_input()
		menu()
	elif pilih == 3:
		os.system('cls')
		print("TAMPIL DATA MAHASISWA ")
		baris = 1;
		for data in dataSiswa:
			print("Data ke ", baris)
			print("Nama : "+data[0])
			print("Nim  : "+str(data[1]))
			print("--------------------------")
			baris = baris+1
		updt = raw_input("Masukkan data yang akan di update : ")
		os.system('cls')
		
	elif pilih == 5 :
		author()
		menu()
	elif pilih == 6 :
		sys.exit()

def author():
	os.system('cls')
	print("alvin meko | 672010193")
	print("uksw 2015")

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		siswa = []
		print("INPUT DATA MAHASISWA ")
		siswa.append(raw_input("masukkan nama siswa : "))
		siswa.append(int(input("masukkan nim : ")))
		dataSiswa.append(siswa)
		ulang = raw_input("Apakah Anda Ingin Mengulang (Y/ T)? ")		

menu()
