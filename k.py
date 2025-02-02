import itertools
def generate():
    user = input("Выведите строку:")
    y = itertools.permutations(user)
    for x in y:
        print(''.join(x))

generate()
