def get_data():
    data = []
    for i in range(4):
        data.append(input())

    return data


def main():
    data = get_data()

    for i, d in enumerate(data):
        d = float(d)
        data[i] = format(d, '.2f')

    for spec in ['>7', '<7']:
        for i in range(0, len(data), 2):
            f = format(data[i], spec)
            s = format(data[i+1], spec)
            print('|{}   {}|'.format(f, s))


if __name__ == '__main__':
    main()
