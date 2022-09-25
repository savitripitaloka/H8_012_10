print("**************************************************************************************")
print("*************************KONVERSI ANGKA MENJADI TERBILANG*****************************")
print("**************************************************************************************")

def terbilang_puluhan(angka):
    angka_terbilang = {
        1: 'Satu',
        2: 'Dua',
        3: 'Tiga',
        4: 'Empat',
        5: 'Lima',
        6: 'Enam',
        7: 'Tujuh',
        8: 'Delapan',
        9: 'Sembilan',
        10: 'Sepuluh', 
        11: 'Sebelas'
    }
    puluhan = angka // 10
    sisa = angka % 10
    result = []
    

    satuan = sisa % 10
    if puluhan == 1:
        if satuan == 0:
            result.append(angka_terbilang[10])
        elif satuan == 1:
            result.append(angka_terbilang[11])
        else:
            result.append(angka_terbilang[satuan])
            result.append('Belas')
        satuan = 0      
    elif puluhan > 0:
        result.append(angka_terbilang[puluhan])
        result.append('Puluh')
        
    if satuan > 0:
        result.append(angka_terbilang[satuan])
    

    return ' '.join(result)
    

def terbilang(angka):
    if angka == 0:
        return 'Nol'
    
    result = []
    sisa = angka

    if sisa > 0:
        result += [terbilang_puluhan(sisa)]

    result = ' '.join(result)

    return result


def main():
    lanjut = 1
    while(lanjut > 0):
        lanjut += 1
        angka = int(input('\nMasukkan angka (antara 0 - 99) : '))
        print(terbilang(angka))


if __name__ == '__main__':
    main()