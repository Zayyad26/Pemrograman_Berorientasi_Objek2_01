try:
    # Ambil input dari user
    angka = int(input("Masukkan angka: "))

    # Bagi dengan 2
    hasil = angka / 2

except ValueError:
    # Jika terjadi ValueError saat mengkonversi input ke integer
    print("Input yang dimasukkan harus berupa angka!")

except:
    # Jika terjadi kesalahan yang tidak diketahui
    print("Terjadi kesalahan yang tidak diketahui!")

else:
    # Jika tidak terjadi kesalahan pada blok try
    print("Hasil pembagian adalah:", hasil)
