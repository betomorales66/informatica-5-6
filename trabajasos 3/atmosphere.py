def main():

    layer = input("descent atmosphere layer:")

    if layer == "exosphere":
        print("your altittude level will be between 700 and 10,000 km")

    elif layer == "thermosphere":
            print("your altittude level will be between 85 and 700 km km")

    elif layer == "mesosphere":
            print("your altittude level will be between 50 and 85 km")

    elif layer == "stratosphere":
            print("your altittude level will be between 12 and 50 km")

    elif layer == "troposphere":
            print("your altittude level will be between 0 and 12 km")

    else:
          print("ERR0R 😡")

    altittude = int(input("Enter exact altittude:"))
#troposphere
    if altittude > 0:
        print(altittude - 0 / 0.02 )
#stratosphere
    elif altittude > 12:
        print(altittude - 12 / 0.075 )
#mesosphere
    elif altittude > 50:
        print(altittude - 50 / 0.2 )
#thermosphere
    elif altittude > 85:
        print(altittude - 85 / 0.5 )
#exosphere
    elif altittude > 700:
        print(altittude - 700 / 2 )

    elif altittude > 10000:
        print("you in space now buddy")

    else:
        print("error")




















if __name__=="__main__":
    main()
