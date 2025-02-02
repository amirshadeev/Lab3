def pali(user):
    if user == user[::-1]:
        print("palindrom")
    else:print("not palindrome")
user = input("Выведите слово:")
pali(user)