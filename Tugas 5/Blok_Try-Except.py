try:
    # Ambil input dari user
    bilangan = int(input("Masukkan bilangan bulat: "))

    # Bagi dengan 2
    hasil = bilangan / 2

    # Print hasil pembagian
    print("Hasil pembagian adalah:", hasil)

except ValueError:
    # Jika terjadi ValueError saat mengkonversi input ke integer
    print("Input yang dimasukkan harus berupa bilangan bulat!")

except ZeroDivisionError:
    # Jika terjadi ZeroDivisionError saat melakukan pembagian dengan angka 0
    print("Tidak dapat melakukan pembagian dengan angka 0!")

except Exception as e:
    # Jika terjadi kesalahan yang tidak diketahui
    print("Terjadi kesalahan:", e)

else:
    # Jika tidak terjadi kesalahan pada blok try
    print("Program selesai")

finally:
    # Menutup program
    print("Program selesai")
