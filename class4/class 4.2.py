def octalToDecimal(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp:
        last_digit = temp % 10
        temp = temp // 10
        dec_value += last_digit * base
        base = base * 8
    return dec_value

def decToHexa(n):
    hexaDeciNum = '' 
    while n != 0:
        temp = 0
        temp = n % 16
        if temp < 10:
            hexaDeciNum = str(temp) + hexaDeciNum
        else:
            hexaDeciNum = chr(temp + 87) + hexaDeciNum
        n = n // 16
    return hexaDeciNum

# Driver code
if __name__ == '__main__':
    octnum = 7321
    decnum = octalToDecimal(octnum)
    hexnum = decToHexa(decnum)
    print("Equivalent Hexadecimal Value = {}".format(hexnum))