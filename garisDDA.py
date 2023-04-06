import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    # Menghitung delta x dan delta y
    dx = x2 - x1
    dy = y2 - y1
    
    # Menghitung jumlah langkah
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    # Menghitung penambahan x dan y pada setiap langkah
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Menginisialisasi titik awal
    x = x1
    y = y1
    
    # Membuat list untuk menyimpan koordinat x dan y
    x_vals = []
    y_vals = []
    
    # Melakukan iterasi untuk menghitung koordinat setiap langkah
    for i in range(steps):
        x_vals.append(x)
        y_vals.append(y)
        x += x_inc
        y += y_inc
    
    # Menggambar garis menggunakan library matplotlib
    plt.plot(x_vals, y_vals)
    plt.show()

# Input titik awal dan titik akhir garis
x1 = int(input("Masukkan koordinat x1: "))
y1 = int(input("Masukkan koordinat y1: "))
x2 = int(input("Masukkan koordinat x2: "))
y2 = int(input("Masukkan koordinat y2: "))

# Memanggil fungsi dda dengan parameter yang diinputkan
dda(x1, y1, x2, y2)
