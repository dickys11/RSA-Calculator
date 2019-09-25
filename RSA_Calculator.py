import math
from tkinter import *


def hitung(p, q):
    n = p*q
    # print(n)

    z = (p-1)*(q-1)
    # print(z)

    list_e = []
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            list_e.append(i)
    print('Nilai e yang mungkin:')
    for nilai in list_e:
        print(nilai)

    e = int(input('Pilih e: '))
    if e not in list_e:
        print('Eror, mohon masukkan bilangan dari pilihan yang tersedia.')
        exit()
    else:
        for i in range(2, n):
            if (e*i) % z == 1 and i != e:
                d = i
                # print(d)
                break

    print('\n--------------------------')
    print('p = {}'.format(p))
    print('q = {}'.format(q))
    print('n = {}'.format(n))
    print('z = {}'.format(z))
    print('e = {}'.format(e))
    print('d = {}'.format(d))
    print('\n')
    print('Kunci publik = ({}, {})'.format(e, n))
    print('Kunci privat = ({}, {})'.format(d, n))


def cek_prima(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # prima
                return FALSE
                break
        else:
            # prima
            return TRUE
    else:
        # bukan prima
        return FALSE


p = int(input('Masukkan Nilai p: '))
q = int(input('Masukkan Nilai q: '))
if cek_prima(p) and cek_prima(q):
    hitung(p, q)
else:
    print('p atau q bukan bilangan prima, mohon masukkan bilangan prima.')
