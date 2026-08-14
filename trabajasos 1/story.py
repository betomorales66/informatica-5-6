def main():
    # planet = input("Planet: ")

    # # separation
    # print("Hello", planet, "hello")

    # # Ending
    # print("hello", end=" ")
    # print(planet)

    # # Concatenation
    # print("hello " + planet)

    # # Formatted String
    # print(f"hello {planet}")

    name = input ("what is your name? ").title().strip()
    color = input("tell me a color: ").lower().strip()
    adj = input("tell me an adjective: ")
    goal = input("tell me a goal you want to achieve: ")

    print()
    print("hello", name, "!" )
    print()
    print("this is your story")
    print()
    print("At dawn the sky turned", color)
    print("and the air felt", adj,".")
    print("I decided today I will finally", goal)


    print()
    print("HELL0", name .upper(), "!" )
    print()
    print("THIS IS YOUR STORY!")
    print()
    print("AT DAWN THE SKY TURNED", color .upper())
    print("AND THE AIR FELT", adj .upper(),".")
    print("I DECIDED TODAY I WILL FINALLY", goal .upper())








if __name__ == "__main__":
    main()
