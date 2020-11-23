# Импорт модуля random
import random
# Создаем функцию pass_gen
def pass_gen(length):
    digits='1234567890'
    leters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leters_2='abcdefghijklmnopqrstuvwxyz'
    symbols='!@#$%^&*()-+'
    password=''
    var=[digits,leters,leters_2,symbols]
# Генерация пароля
    if length<12:
        return print('Ошибка! Пароль должен иметь не менее 12 символов')
    else:
        password+=random.choice(digits)
        password+=random.choice(leters)
        password+=random.choice(leters_2)
        password+=random.choice(symbols)
        while len(password)<length:
            password+=random.choice(var[random.randint(0,3)])
        print(password)
pass_gen(12)
