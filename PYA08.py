def main():
    string = input()
    for c in string:
        print('ASCII code for \'{}\' is {}'.format(c, ord(c)))

    print(sum([ord(c) for c in string]))


if __name__ == '__main__':
    main()
