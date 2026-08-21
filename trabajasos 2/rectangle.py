def main():
    width = int(input("enter the width of the rectagle: "))
    print("o" * width)
    print("o" * width)
    print("o" * width)
    print("o" * width)
    print("o" * width)

    p = (width * 2)+(5 * 2)
    print("perimeter:", p)

    a = (5 * width)
    print("area:", a)

    d = ((5**2 + width**2)**0.5)
    print("diagonal:", d)



if __name__=="__main__":
    main()
