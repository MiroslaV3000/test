import numpy

class IEEE754Number:
    Bite = 0
    exp = None
    segregation = None
    mantisa = None

    def __init__(self, exp, segregetion, mantisa):
        self.exp = exp
        self.exponent = segregetion
        self.mantisa = mantisa

    def print(self):
        print(f'IEEE 754 {self.Bite}|{self.exp}|{self.mantisa}')
def direct(direcct1, direcct2):
    sum_result = numpy.empty(8, dtype=object)
    transport = 0
    for i in range(7, -1, -1):
        disparation = direcct1[i] + direcct2[i] + transport
        if disparation == 0:
            transport = 0
            sum_result[i] = 0
        elif disparation == 1:
            transport = 0
            sum_result[i] = 1
        elif disparation == 2:
            transport = 1
            sum_result[i] = 0
        elif disparation == 3:
            transport = 1
            sum_result[i] = 1
    return sum_result
def directarion(number):
    directation = numpy.empty(8, dtype=object)
    if number < 0:
        directation[0] = 1
        number = abs(number)
    else:
        directation[0] = 0
    if abs(number) >= 127:
        for i in range(7, -1, -1):
            directation[i] = number % 2
            number //= 2
        return directation
    else:
        for i in range(7, 0, -1):
            directation[i] = number % 2
            number //= 2
    return directation

def invertate(Binary):
    if Binary[0] == 1:
        for i in range(7, 0, -1):
            if Binary[i] == 0:
                Binary[i] = 1
            else:
                Binary[i] = 0
    return Binary

def aditional(invertation):
    if invertation[0] == 1:
        for i in range(7, 0, -1):
            if invertation[i] == 0:
                invertation[i] = 1
                return invertation
            else:
                invertation[i] = 0
    return invertation



def additionlist_sum(aditional1, aditional2):
    result = direct(aditional1, aditional2)
    if result[0] == 1:
        invertate(result)
        aditional(result)
    return result

def subtraction(aditional1, aditional2):
    if aditional2[0] == 1:
        for i in range(7, 0, -1):
            if aditional2[i] == 1:
                aditional2[i] = 0
                break
            else:
                aditional2[i] = 1
        aditional2 = invertate(aditional2)
        aditional2[0] = 0
    else:
        if_zero_aditional2 = True
        for i in aditional2:
            if i == 1:
                if_zero_aditional2 = False
        if if_zero_aditional2:
            return additionlist_sum(aditional1, aditional2)
        aditional2[0] = 1
        aditional2 = invertate(aditional2)
        aditional2 = aditional(aditional2)
    return additionlist_sum(aditional1, aditional2)
def division(dividend_local, divisor_local):
    dividentation = ''.join(map(str, dividend_local))
    dividentation = dividentation.lstrip('0')
    divis_int = ''.join(map(str, divisor_local))
    divis_int = divis_int.lstrip('0')
    dec_num1 = int(dividentation, 2)
    dec_num2 = int(divis_int, 2)
    result_division = dec_num1 / dec_num2
    int_part = bin(int(result_division))[2:]
    frac = result_division - int(result_division)
    frac_bin = ''
    for _ in range(5):
        frac *= 2
        digitt = int(frac)
        frac_bin += str(digitt)
        frac -= digitt
    binary_result = int_part + '.' + frac_bin
    return binary_result
def move(amount, directtation):
    result_of_moving = numpy.zeros(8, dtype=object)
    result_of_moving[0] = directtation[0]
    for i in range(7, 1, -1):
        result_of_moving[i - amount] = directtation[i]
    return result_of_moving

def multiplication(diirect1, diirect2):
    result = numpy.zeros(8, dtype=object)
    for i in range(7, 0, -1):
        if diirect2[i] == 1:
            result = direct(result, move(7 - i, diirect1))
    if diirect1[0] == 1 and diirect2[0] == 1:
        result[0] = 0
    elif diirect1[0] == 1 and diirect2[0] == 0:
        result[0] = 1
    elif diirect1[0] == 0 and diirect2[0] == 1:
        result[0] = 1
    elif diirect1[0] == 0 and diirect2[0] == 0:
        result[0] = 0
    return result

def comparison(dir1, dir2):
    return int(''.join(map(str, dir1))) < int(''.join(map(str, dir2)))

def decimal(number, prebulp=5):
    binary_str_line = format(number, '0{}b'.format(prebulp))
    return binary_str_line



def float_binary(float_numerate):
    if float_numerate == 0:
        return '0'

    float_numerate = abs(float_numerate)
    integer_part = int(float_numerate)
    decimal_part = float_numerate - integer_part

    if integer_part != 0:
        binary_integeration = ''.join(map(str, directarion(integer_part)))
        binary_integeration = binary_integeration.lstrip('0')
    else:
        binary_integeration = '0'

    decimal = ''
    while decimal_part > 0:
        decimal_part *= 2
        if decimal_part >= 1:
            decimal += '1'
            decimal_part -= 1
        else:
            decimal += '0'

    binary_result = binary_integeration + '.' + decimal
    return binary_result


def normalize(binary_number):
    dot_position = binary_number.index('.')
    exponent = dot_position - 1
    normalization = binary_number.replace('.', '')
    normalization = normalization[:1] + '.' + normalization[1:]
    return normalization, exponent

def ieee754(binary_number):
    normalized, exponent = normalize(binary_number)
    binary_exponent = ''.join(map(str, directarion(exponent + 127)))
    mantissa = normalized[2:]
    while len(mantissa) != 23:
        mantissa = mantissa + '0'
    ieee754_number = IEEE754Number(binary_exponent, exponent, mantissa)
    return ieee754_number
def ieee754(ieee_1: IEEE754Number, ieee_2: IEEE754Number):
    if int(ieee_1.exponent) > int(ieee_2.exponent):
        mantissa_first = '1.' + ieee_1.mantisa
        mantissa_second_of_ieee = '1.' + ieee_2.mantisa
        difference_exponent = ieee_1.exponent - ieee_2.exponent
        mantissa_second_of_ieee = normalize_mantissa(mantissa_second_of_ieee, difference_exponent)
        sum_result = mantissa_sum_of_bynary(mantissa_first, mantissa_second_of_ieee)
        sum_result = sum_result[2:]
        while len(sum_result) != 23:
            sum_result = sum_result + '0'
        exponent_bits = ieee_1.exp[:-2]
        exponent_bits = exponent_bits + '10'
        ieee754_sum_result = IEEE754Number(exponent_bits, ieee_1.exponent, sum_result)
        ieee754_sum_result.print_info()
def normalize(mantissa, difference_exponent):
    normalized_mantis = mantissa.replace('.', "")
    for _ in range(difference_exponent - 1):
        normalized_mantis = '0' + normalized_mantis
    normalized_mantis = '.' + normalized_mantis
    normalized_mantis = '0' + normalized_mantis
    return normalized_mantis

def string_to_numpy(mantissa):
    mantissa_ind = len(mantissa) - 1
    numpy_mantissa = numpy.zeros(8, dtype=object)
    for i in range(7, 7 - len(mantissa), -1):
        numpy_mantissa[i] = int(mantissa[mantissa_ind])
        mantissa_ind -= 1
    return numpy_mantissa

def mantissa_sum_of_bynary(mantissa_first, mantissa_second):
    first_integer = mantissa_first[0]
    second_integer = mantissa_second[0]
    first_decimal = mantissa_first[2:8]
    second_decimal = mantissa_second[2:8]
    first_integer = string_to_numpy(first_integer)
    second_integer = string_to_numpy(second_integer)
    first_decimal = string_to_numpy(first_decimal)
    second_decimal = string_to_numpy(second_decimal)
    integer_sum = additionlist_sum(first_integer, second_integer)
    decimal_sum = additionlist_sum(first_decimal, second_decimal)
    transitional = numpy.zeros(8, dtype=object)
    transitional[7] = decimal_sum[1]
    integer_sum = additionlist_sum(integer_sum, transitional)
    integer_sum = ''.join(map(str, integer_sum))
    integer_sum = integer_sum.lstrip('0')
    decimal_sum = ''.join(map(str, decimal_sum))
    decimal_sum = "" + decimal_sum[2:]
    mantissa_sum_result = integer_sum + '.' + decimal_sum
    return mantissa_sum_result




