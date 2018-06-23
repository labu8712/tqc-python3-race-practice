def main():
    number = 0
    numbers = []

    while number != 9999:
        number = int(input())
        numbers.append(number)

    print(min(numbers))


if __name__ == '__main__':
    main()
