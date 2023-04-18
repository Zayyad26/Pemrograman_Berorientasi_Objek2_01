try:
    # kode program yang mungkin menghasilkan exception
    x = 1/0 # contoh exception pembagian dengan nol
except ZeroDivisionError:
    # menangani exception ZeroDivisionError
    print("Terdapat kesalahan pembagian dengan nol!")
finally:
    # blok finally selalu dijalankan, baik terjadi exception atau tidak
    print("Program selesai!")
