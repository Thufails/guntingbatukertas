import random

print('Pilihlah jagoanmu')
print('=================')
print('1. Batu')
print('2. Gunting')
print('3. Kertas')
print('=================')

def mainnya () :    
    main = input('Masukkan jagoanmu(1/2/3) : ')
    komputer = random.choice (['Batu', 'Gunting', 'Kertas'])
    if main == '1':
        print('Kamu     : Batu')
        print('Komputer : ',komputer)
        if komputer == 'Batu':
            print('\t Seri')
        if komputer == 'Gunting':
            print('\t Kamu Menang')
        if komputer == 'Kertas':
            print('\t Kamu Kalah')
    if main == '2':
        print('Kamu     : Gunting')
        print('Komputer : ',komputer)
        if komputer == 'Batu':
            print('\t Kamu Kalah')
        if komputer == 'Gunting':
            print('\t Seri')
        if komputer == 'Kertas':
            print('\t Kamu Kalah')
    if main == '3':
        print('Kamu     : Kertas')
        print('Komputer : ',komputer)
        if komputer == 'Batu':
            print('\t Kamu Menang')
        if komputer == 'Gunting':
            print('\t Kamu Kalah')
        if komputer == 'Kertas':
            print('\t Seri')
    if main >= '4':
        print('Pilihanmu Salah')
mainnya()
