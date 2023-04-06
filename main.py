import matplotlib.pyplot as plt


def draw_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / steps
    y_increment = dy / steps
    x, y = x1, y1
    points = [(round(x), round(y))]
    for i in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))
    return points


def draw_bresenham(x1, y1, x2, y2):
    # Menghitung delta x dan delta y
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Menghitung Nilai Increment Pada x dan y
    x_sign = 1 if x2 > x1 else -1
    y_sign = 1 if y2 > y1 else -1
    if dy <= dx:
        slope_error = dx / 2.0
        y = y1
        points = []
        for x in range(x1, x2 + x_sign, x_sign):
            points.append((x, y))
            slope_error -= dy
            if slope_error < 0:
                y += y_sign
                slope_error += dx
    else:
        slope_error = dy / 2.0
        x = x1
        points = []
        for y in range(y1, y2 + y_sign, y_sign):
            points.append((x, y))
            slope_error -= dx
            if slope_error < 0:
                x += x_sign
                slope_error += dy
    return points


def draw_circle(xc, yc, r):
    x, y = r, 0
    points = []
    decision = 1 - r
    while x >= y:
        points.append((xc + x, yc + y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc - x, yc + y))
        points.append((xc - x, yc - y))
        points.append((xc - y, yc - x))
        points.append((xc + y, yc - x))
        points.append((xc + x, yc - y))
        y += 1
        if decision <= 0:
            decision += 2 * y + 1
        else:
            x -= 1
            decision += 2 * (y - x) + 1
    return points


def plot_points(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, 'o')
    plt.show()


def main():
    options = ["Garis DDA", "Garis Bresenham", "Lingkaran"]
    print("Pilih opsi:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input("Masukkan pilihan: "))
    if choice == 1:
        x1, y1 = map(int, input(
            "Masukkan koordinat titik awal (pisahkan dengan spasi): ").split())
        x2, y2 = map(int, input(
            "Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split())
        points = draw_dda(x1, y1, x2, y2)
        plot_points(points)

    elif choice == 2:
        x1, y1 = map(int, input(
            "Masukkan koordinat titik awal (pisahkan dengan spasi): ").split())
        x2, y2 = map(int, input(
            "Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split())
        points = draw_bresenham(x1, y1, x2, y2)
        plot_points(points)

    elif choice == 3:
        xc, yc = map(int, input(
            "Masukkan koordinat titik pusat (pisahkan dengan spasi): ").split())
        r = map(int, input("Masukkan jari-jari: "))
        points = draw_circle(xc, yc, r)
        plot_points(points)


main()
