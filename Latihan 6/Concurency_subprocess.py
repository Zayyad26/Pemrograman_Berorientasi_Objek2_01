import subprocess

# Menjalankan perintah ls (Unix/Linux) atau dir (Windows)
result = subprocess.run(['ls'], capture_output=True, text=True, check=True)

# Mencetak output
print("Output:\n", result.stdout)

# Mengecek kode keluaran
print("Kode Keluaran:", result.returncode)
