try:
    # Buka file
    file = open("contoh.txt", "r")

    # Baca isi file
    isi = file.read()

except FileNotFoundError:
    # Jika file tidak ditemukan
    print("File tidak ditemukan!")

except:
    # Jika terjadi kesalahan yang tidak diketahui
    print("Terjadi kesalahan yang tidak diketahui!")

else:
    # Jika tidak terjadi kesalahan pada blok try
    print("Isi file adalah:")
    print(isi)

finally:
    # Tutup file, terlepas dari apapun yang terjadi
    file.close()
