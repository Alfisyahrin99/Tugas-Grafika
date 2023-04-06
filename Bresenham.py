import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    # Menghitung delta x dan delta y
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Menghitung nilai increment pada x dan y
    if x1 < x2:
        x_inc = 1
    else:
        x_inc = -1
    
    if y1 < y2:
        y_inc = 1
    else:
        y_inc = -1
    
    # Menghitung nilai konstanta untuk keputusan piksel
    if dx > dy:
        p = 2 * dy - dx
    else:
        p = 2 * dx - dy
    
    # Menginisialisasi titik awal
    x = x1
    y = y1
    
    # Membuat list untuk menyimpan koordinat x dan y
    x_vals = []
    y_vals = []
    
    # Melakukan iterasi untuk menghitung koordinat setiap piksel
    while x != x2 or y != y2:
        x_vals.append(x)
        y_vals.append(y)
        
        if dx > dy:
            if p >= 0:
                y += y_inc
                p -= 2 * dx
            
            x += x_inc
            p += 2 * dy
        else:
            if p >= 0:
                x += x_inc
                p -= 2 * dy
            
            y += y_inc
            p += 2 * dx
    
    # Menggambar garis menggunakan library matplotlib
    plt.plot(x_vals, y_vals)
    plt.show()

# Input titik awal dan titik akhir garis
x1 = int(input("Masukkan koordinat x1: "))
y1 = int(input("Masukkan koordinat y1: "))
x2 = int(input("Masukkan koordinat x2: "))
y2 = int(input("Masukkan koordinat y2: "))

# Memanggil fungsi bresenham dengan parameter yang diinputkan
bresenham(int(x1), int(y1), int(x2), int(y2))
