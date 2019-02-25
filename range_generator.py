def MyRange(start, stop, step):
    counter = start
    while counter < (stop):
        yield counter
        counter += step

def my_range(start, stop, step):
    counter = start
    call = MyRange(start, stop, step)
    while counter <= (stop - step):
        counter += step
        print(next(call))


