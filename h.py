def convert(Fahrenheit):
    Celsius = (5 / 9) * (Fahrenheit - 32)
    print(f"Цельсия:{Celsius:.3f}")

Fahrenheit = float(input("Выведите фаренгейт:"))
convert(Fahrenheit)
