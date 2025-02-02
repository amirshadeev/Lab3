def sphere(rad):
    Volume = (4/3)*3.14*(rad**3)
    print(f"Обьем сферы:{Volume:.3f}")

rad = float(input("Ваш радиус:"))
sphere(rad)