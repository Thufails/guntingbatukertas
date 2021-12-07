print('==========')
print('Andi Lapar')
print('==========')

masak = input('Apakah Andi mood masak ? (iya/tidak)')

if masak == 'tidak':
    print('sudahlah Andi males')
elif masak == 'iya':
    telur = input('apakah ada telur? (iya/tidak)')
    if telur == 'iya':
        print('masak telur')
    else:
        pass
    
    bayam = input('apakah ada bayam? (iya/tidak)')
    if bayam == 'iya':
        print('masak bayam')
    else:
        pass

    if telur == 'iya' and bayam == 'iya':
        print('maka andi masak telur dan bayam')
    elif telur == 'iya' and bayam == 'tidak':
        print('maka andi masak telur saja')
    elif telur == 'tidak' and bayam == 'iya':
        print('maka andi masak bayam saja')
    elif telur == 'tidak' and bayam == 'tidak':
        print('hiya hiya miskin')
    else:
        print('salah jawaban uyy')
else:
    print('salah jawaban')