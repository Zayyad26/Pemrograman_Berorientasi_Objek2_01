try:
    # Potong string menjadi 3 karakter
    string = "abcde"
    substring = string[:3]

    # Konversi string ke integer
    integer = int(substring)

    # Print hasil konversi
    print("Hasil konversi adalah:", integer)

except ValueError:
    # Jika terjadi ValueError (gagal mengkonversi string ke integer)
    print("Terjadi kesalahan konversi!")

except:
    # Jika terjadi kesalahan yang tidak diketahui
    print("Terjadi kesalahan yang tidak diketahui!")
