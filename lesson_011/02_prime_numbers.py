# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    pass
    # TODO здесь ваш код


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
    print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    pass
    # TODO здесь ваш код


for number in prime_numbers_generator(n=10000):
    print(number)


# Усложненное задание (делать по желанию)
# Преобразовать итератор/генератор так, чтобы он выдавал только "счастливые" простые числа
# у которых сумма первых цифр равна сумме последних
# Если простое число имеет нечетное число цифр (например 727 или 92083),
# то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#   727 -> 7(2)7 -> 7 == 7 -> True
#   92083 -> 92(0)83 -> 9+2 == 8+3 -> True

