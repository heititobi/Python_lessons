# General ruling for Estonian ID - https://et.wikipedia.org/wiki/Isikukood
from random import randint


# Generates random string of number taking the range and the needed number of digits as an input
def number(start, stop, digits=1):
    random_number = str(randint(start, stop))
    return random_number.zfill(digits)


# Mathematical calculation of Estonian ID number and its modulo 11 for the last digit of the ID
def modulo_11(code, step=1):
    first_step = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_step = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    modulo = 0
    if step == 1:
        for index, element in enumerate(str(code)):
            modulo += int(element) * first_step[index]
    else:
        print("Step2")
        for index, element in enumerate(str(code)):
            modulo += int(element) * second_step[index]
    return str(modulo % 11)


# Calculates Estonian ID-s last digit checksum based on first 10 digits
def checksum_calculation(id_number):
    checksum = modulo_11(id_number)
    if int(checksum) != 10:
        return checksum
    else:
        return modulo_11(id_number, step=2)


# Generates random Estonian ID code GYYMMDDSSSC and returns it as a string. G shows sex and century of birth,
# SSS is a serial number separating persons born on the same date and C a checksum
def estonian_id():
    gender = number(1, 6)
    year = number(0, 99, 2)
    month = number(1, 12, 2)
    day = number(1, 28, 2)
    serial_number = number(0, 999, 3)
    first_ten_id_numbers = f'{gender}{year}{month}{day}{serial_number}'
    return f'{first_ten_id_numbers}{checksum_calculation(first_ten_id_numbers)}'


print(estonian_id())
