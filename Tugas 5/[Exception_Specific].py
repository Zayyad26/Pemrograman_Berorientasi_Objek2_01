try:
    # melakukan pembagian
    x = 10 / 0
except ZeroDivisionError:
    # menangani kesalahan pembagian dengan nol
    print("Tidak dapat melakukan pembagian dengan nol.")
except TypeError:
    # menangani kesalahan tipe data
    print("Tipe data yang tidak sesuai.")
except Exception as e:
    # menangani kesalahan umum
    print(f"Terjadi kesalahan: {e}")
