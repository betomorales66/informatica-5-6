def main():
    print("Binary to Decimal Converter")
    print("The purpose of this program is to help the people convert binary numbers into decimal numbers")
    binary = (input("Enter a binary number:" ))
    decimal = binary_to_decimal(binary)
    print("decimal number:", decimal)


def binary_to_decimal (binary):
    decimal = 0
    for digit in decimal:
        decimal = decimal * 2 + int(digit)







if __name__=="__main__":
    main()
