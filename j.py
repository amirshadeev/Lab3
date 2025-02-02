def sfilter(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
ourlist = input("Выведите список:").split()
ourlist = list(map(int, ourlist))
result = list(filter(lambda y:sfilter(y),ourlist)) 
print(f"Результат:{result}")   