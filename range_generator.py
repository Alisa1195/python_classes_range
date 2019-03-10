def MyRange(start, stop, step):
    counter = start
    while True:
        yield counter
        counter += step


def my_range(*args):
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

    counter = start
    call = MyRange(start, stop, step)
    while counter <= (stop - step):
        counter += step
        print(next(call))

my_range(0, 10, 2)
print("----")
my_range(10)