from random import randint

#General ruling for Estonian ID - https://et.wikipedia.org/wiki/Isikukood
# 1. = sugu ja sünniaasta esimesed kaks numbrit (1...6)
# 2. ja 3. = sünniaasta 3. ja 4. numbrid (00...99)
# 4. ja 5. = sünnikuu (01...12)
# 6. ja 7. = sünnikuupäev (01...31)
# 8., 9. ja 10. number = järjekorranumber samal päeval sündinute eristamiseks (000...999). Enne 2013. aastat sündinute puhul võib sisaldada haigla tunnust.
# 11. = kontrollnumber (0...9)

# Generates random string of number taking the range and the needed number of digits as an input
def number(start, stop, digits=1):
    random_number = str(randint(start, stop))
    return random_number.zfill(digits)

# Calculates Estonian ID-s last digit checksum based on first 10 digits
def checksum_calculation(id):
    first_step = [1,2,3,4,5,6,7,8,9,1]
    second_step = [3,4,5,6,7,8,9,1,2,3]
    checksum_first = 0
    checksum_second = 0
    for index, number in enumerate(id):
        checksum_first += int(number)*first_step[index]
    if checksum_first % 11 == 10:
        for index, number in enumerate(id):
            checksum_second += int(number)*second_step[index]
        return checksum_second if checksum_first % 11 != 10 else 0
    return checksum_first % 11

# Generates random Estonian ID code GYYMMDDSSSC and returns it as a string. G shows sex and century of birth,
# SSS is a serial number separating persons born on the same date and C a checksum
def Estonian_ID():
    gender = number(1,6)
    year = number(0,99,2)
    month = number(1,12,2)
    day = number(1,28,2)
    serial_number = number(0,999,3)
    ID = gender + year + month + day + serial_number
    return f'{ID}{checksum_calculation(ID)}'

print(Estonian_ID())

