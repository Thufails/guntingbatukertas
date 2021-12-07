def print_faktor(x):
    """Fungsi menerima input bilangan dan mencetak faktornya"""
    print("Faktor dari", x, "adalah:")
    for i in range(x, 0, -1):
        if x % i == 0:
            print(i)

num = int(input("Masukkan bilangan: "))
print_faktor(num)

