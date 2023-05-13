import multiprocessing

def square_numbers(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Membagi data menjadi dua bagian
    split = len(numbers) // 2
    numbers1 = numbers[:split]
    numbers2 = numbers[split:]

    # Membuat dua proses multiprocessing
    process1 = multiprocessing.Process(target=square_numbers, args=(numbers1,))
    process2 = multiprocessing.Process(target=square_numbers, args=(numbers2,))

    # Memulai kedua proses
    process1.start()
    process2.start()

    # Menunggu kedua proses selesai
    process1.join()
    process2.join()

    # Mengumpulkan hasil dari kedua proses
    result1 = process1.return_value
    result2 = process2.return_value
    result = result1 + result2

    print("Hasil akhir:", result)
