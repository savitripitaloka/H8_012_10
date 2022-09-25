print("**************************************************************************************")
print("******************************PERMAINAN TEBAK ANGKA***********************************")
print("**************************************************************************************")

print("Saya memikirkan sebuah angka dari 1 - 10")
print("Silakan tebak angka yang saya pikirkan")
print("Input HARUS berupa Angka")
print("Score Anda saat ini 100")

#import bilangan random integer
import random
bil_random = random.randint(1,10)

#looping game
chance = 4
coba = 1
score = 100
while(chance > 0):
    try:
        tebak = int(input("\nMasukkan tebakan Anda :"))
        if tebak == bil_random:
            print("ANDA MENANG")
            print(f"Score Anda {score}.")
            print(f"Jumlah percobaan Anda {coba}.\n")
            break
        elif tebak > bil_random:
            coba += 1
            chance -= 1
            score -= 10
            print("Tebakan Anda terlalu besar, score Anda dikurangi 10")
            print(f"Score Anda saat ini {score}\n")
        else:
            coba += 1
            chance -= 1
            score -= 10
            print("Tebakan Anda terlalu kecil, score Anda dikurangi 10")
            print(f"Score Anda saat ini {score}\n")
        if chance == 0:
            print("GAME OVER")
            print(f"Score Anda {score}.")
            break
    except ValueError as err:
        coba += 1
        chance -= 1
        score -= 20
        print("Tebakan harus berupa angka")
        print("Penalti, poin dikurangi 20")
        print(f"Score Anda saat ini {score}\n")