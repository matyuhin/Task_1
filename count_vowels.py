vowels = ('a', 'o', 'u', 'i', 'e', 'y')
text = input("Введите строку: ").lower()
for letter in vowels:
    print(letter, text.count(letter), end=', ')
