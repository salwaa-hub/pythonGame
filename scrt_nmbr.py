secret_number = 3
guess = 0
guess_count = 3

while guess < guess_count:
    user = int(input("Masukkan angka : "))
    if int(user) == 3:
        print("Anda berhasil!")
        break
    else:
        print("Tebakan Anda salah!")
        guess = guess + 1
else:
    print("Kesempatan Anda habis!")