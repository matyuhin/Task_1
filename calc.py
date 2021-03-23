def computation(num1):
    try:
        result = num1
        lst = input("Для дальнейшего вычисления введите выражение в формате: <операция> <число> \nДля получения результата введите '=': ").split()
        if len(lst) == 2:
            operation, num2 = lst
            if operation == '+':
                result = num1 + float(num2)
            elif operation == '-':
                result = num1 - float(num2)
            elif operation == '*':
                result = num1 * float(num2)
            elif operation == '/':
                result = num1 / float(num2)
            elif operation == '**':
                result = num1 ** float(num2)
            elif operation == '//':
                result = num1 // float(num2)
            elif operation == '%':
                result = num1 % float(num2)
            else:
                raise Exception
            return computation(result)
        elif lst[0] == '=':
            if result % 1 == 0.0:
                result = int(result)
            return print(result)
        else:
            raise ValueError
    except ValueError:
        print("Неверный формат ввода")
    except ZeroDivisionError:
        print("Деление на ноль!")
    except Exception:
        print("Неподдерживаемая операция")


try:
    num1 = float(input("Введите число: "))
    computation(num1)
except ValueError:
    print("Неверный формат ввода")
