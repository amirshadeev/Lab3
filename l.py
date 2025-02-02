def amir():
    user = input("Выведите строку:")
    word = ' '.join(user.split()[::-1])
    print(word)

amir()
