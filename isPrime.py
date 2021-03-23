text = input("Введите целое число: ")
if text.isdigit():
    number = int(text)
    prime = False
    if number % 2 == 0:
        prime = number == 2
    elif number > 1:
        devider = 3
        while devider ** 2 <= number and number % devider != 0 and number > 1:
            devider += 2
        prime = devider ** 2 > number
    if prime:
        print(number, '- простое число')
    else:
        print(number, '- не простое число')
else:
    print("Ошибка: введенные данные не являются целым числом.")
