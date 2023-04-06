import matplotlib.pyplot as plt

def draw_circle(xc, yc, r):
    # Menghitung nilai awal koordinat x dan y
    x = 0
    y = r
    
    # Menghitung nilai awal keputusan piksel
    p = 1 - r
    
    # Membuat list untuk menyimpan koordinat x dan y
    x_vals = []
    y_vals = []
    
    # Melakukan iterasi untuk menggambar setiap piksel
    while x <= y:
        # Menggambar piksel pada setiap kuadran simetris
        x_vals.append(xc + x)
        x_vals.append(xc - x)
        x_vals.append(xc + y)
        x_vals.append(xc - y)
        y_vals.append(yc + y)
        y_vals.append(yc - y)
        y_vals.append(yc + x)
        y_vals.append(yc - x)
        
        # Menghitung nilai keputusan piksel
        if p < 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += 2 * (x - y) + 1
    
    # Menggambar lingkaran menggunakan library matplotlib
    plt.scatter(x_vals, y_vals, s=1)
    plt.axis('equal')
    plt.show()

# Input koordinat pusat lingkaran dan jari-jarinya
xc = int(input("Masukkan koordinat x pusat lingkaran: "))
yc = int(input("Masukkan koordinat y pusat lingkaran: "))
r = int(input("Masukkan jari-jari lingkaran: "))

# Memanggil fungsi draw_circle dengan parameter yang diinputkan
draw_circle(int(xc), int(yc), int(r))
