def main():

    num1 = float(input("select a number: "))
    num2 = float(input("select another number: "))
    sign = input("select a operation symbol: ")


    if sign == "+":
        print(num1 + num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "/":
            print(num1 / num2)
    else:
        print("mala tuya papu 😭")



if __name__=="__main__":
    main()
