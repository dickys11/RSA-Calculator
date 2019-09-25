from tkinter import *
import math

# HITUNGAN
root = Tk()


def calc():
    p = int(a.get())
    q = int(b.get())

    n = p*q
    z = (p-1)*(q-1)

    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            print(e)
            break

    for i in range(2, n):
        if (e*i) % z == 1 and i != e:
            d = i
            print(d)
            break

    Print(n, e, d)


def Print(n, e, d):
    text_output = StringVar()
    text_output.set('Publik ({}, {}), Privat ({}, {})'.format(n, e, n, d))
    text_label = Label(root, textvariable=text_output)
    text_label.pack()


# GUI

root.title('RSA Calculator')
a_label = Label(root, text='Masukkan nilai p')
a_label.pack()

a = Entry(root)
a.pack()

b_label = Label(root, text='Masukkan nilai q')
b_label.pack()

b = Entry(root)
b.pack()

button = Button(root, text='Hitung', command=calc)
button.pack()

root.geometry("200x130")
root.resizable(FALSE, FALSE)
root.mainloop()
