import sys


def tracefunc(frame, event, arg):
    if event == "return":
        print("function: {} , locals: {} ".format(frame.f_code.co_name, frame.f_locals))

    return tracefunc


def foo():
    a = 12
    b = 21
    return a + b

sys.settrace(tracefunc)
foo()
