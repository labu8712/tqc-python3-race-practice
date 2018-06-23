def main():
    number = int(input())
    r = []

    if number % 3 == 0:
        r.append('3')

    if number % 5 == 0:
        r.append('5')

    if len(r) == 0:
        print('{} is not a multiple of 3 or 5.'.format(number))
    else:
        print('{} is a multiple of {}'.format(number, ' and '.join(r)))


if __name__ == '__main__':
    main()
