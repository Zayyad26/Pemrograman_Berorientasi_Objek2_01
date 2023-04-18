try:
    # Ambil input dari user
    angka = int(input("Masukkan angka: "))

    # Bagi dengan nol
    hasil = 10 / angka

    # Print hasil pembagian
    print("Hasil pembagian adalah:", hasil)

except ValueError:
    # Jika terjadi ValueError saat mengkonversi input ke integer
    print("Input yang dimasukkan harus berupa angka!")

except ZeroDivisionError:
    # Jika terjadi ZeroDivisionError saat melakukan pembagian
    print("Tidak dapat melakukan pembagian dengan angka nol!")

except:
    # Jika terjadi kesalahan yang tidak diketahui
    print("Terjadi kesalahan yang tidak diketahui!")
