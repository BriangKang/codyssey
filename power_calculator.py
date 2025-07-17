def main():
    number_input = input("Enter number: ")
    try:
        number = float(number_input)
    except:
        print("Invalid number input.")
        return

    exponent_input = input("Enter exponent: ")
    try:
        exponent = int(exponent_input)
    except:
        print("Invalid exponent input.")
        return

    result = 1
    for _ in range(exponent):
        result = result * number

    print("Result:", result)

if __name__ == "__main__":
    main()
