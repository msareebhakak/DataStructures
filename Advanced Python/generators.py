def cube(n):
    for i in range(n):
        yield i ** 3


# infinite sequence
def square(n):
    result = n
    while True:
        yield result
        result *= 2


if __name__ == '__main__':
    values = cube(30)
    print(next(values))
    print(next(values))
    print(next(values))
    print(next(values))

    for x in values:
        print(x)

    squares = square(2)
    for count, value in enumerate(squares):
        if count == 100:
            break
        else:
            print(value)
