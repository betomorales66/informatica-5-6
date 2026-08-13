def main():
    planet = input("Planet: ")

    # separation
    print("Hello", planet, "hello")

    # Ending
    print("hello", end=" ")
    print(planet)

    # Concatenation
    print("hello " + planet)

    # Formatted String
    print(f"hello {planet}")


if __name__ == "__main__":
    main()
