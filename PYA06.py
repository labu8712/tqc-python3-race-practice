def get_data():
    data = []
    for i in range(5):
        data.append(input())

    return data


def build_dict():
    keys = ['A', *[str(i) for i in range(2, 11)], 'J', 'Q', 'K']
    values = list(range(1, 14))
    return {k: v for k, v in zip(keys, values)}


def main():
    data = get_data()
    target = build_dict()
    result = sum([target[i] for i in data])
    print(result)


if __name__ == '__main__':
    main()
