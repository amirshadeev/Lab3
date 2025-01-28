def prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
x = input("Введите числа через пробелы:").split()
x = list(map(int, x))
result = list(filter(lambda y:prime(y), x))
print(f"result:{result}")
