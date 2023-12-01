import random


def main():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for r in range(3):
        for c in range(4):
            values[r][c] = random.randint(1, 100)

    print(values)


if __name__ == '__main__':
    main()
