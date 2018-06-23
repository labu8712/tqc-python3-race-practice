def main():
    with open('read.txt', encoding='utf-8') as f:
        _file = f.read()

    print(sum([int(n) for n in _file.split(' ')]))


if __name__ == '__main__':
    main()
