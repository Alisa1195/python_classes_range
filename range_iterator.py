class MyRangeIter:

    def __init__(self, start, stop, step):
        self.current_val = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_val <= (self.stop - self.step):
            self.current_val += self.step
            return self.current_val


def my_range(start, stop, step):
    counter = start
    call = MyRangeIter(start, stop, step)
    print(start)
    while counter < (stop - step):
        counter += step
        print(next(call))

