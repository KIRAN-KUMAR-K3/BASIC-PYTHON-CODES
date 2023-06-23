#2 B) Develop a python program to convert binary to decimal, octal to hexadecimal using funtions.

#Binary to Decimal

def BinaryToDecimal(num):
    expo =1
    dec_num=0
    while(num):
        digit=num%10
        num = int(num/10)

        dec_num+=digit*expo
        expo=expo*2
    return dec_num

#Taking user input
num = int(input("Enter a binary number:"))

#Displaying Output
print("The decimal value is ")