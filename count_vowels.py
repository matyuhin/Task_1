vowels = ('a', 'o', 'u', 'i', 'e', 'y')
text = input("Введите строку: ").lower()
for letter in vowels:
    if letter != 'y':
        print(letter, text.count(letter), end=', ')
    else:
        print(letter, text.count(letter))
