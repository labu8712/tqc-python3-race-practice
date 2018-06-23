def main():
    start = int(input())
    end = int(input())

    result = sum([i for i in range(start, end+1, 2)])
    print(result)


if __name__ == '__main__':
    main()
