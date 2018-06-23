def get_data(i):
    number = 0
    result = []
    print('Create tuple{}:'.format(i))

    while number != -9999:
        number = int(input())
        result.append(number)

    return tuple(result[:-1])


def main():
    tuple1 = get_data(1)
    tuple2 = get_data(2)
    _tuple = (*tuple1, *tuple2)

    print('Combined tuple before sorting: {}'.format(_tuple))
    print('Combined list after sorting: {}'.format(sorted(list(_tuple))))


if __name__ == '__main__':
    main()
