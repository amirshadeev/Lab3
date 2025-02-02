def hist(gam):
    for x in gam:
        print(x*"*")
gam = input("Выведите лист:").split()
gam = list(map(int,gam))
hist(gam)
