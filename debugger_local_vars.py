import sys


def tracefunc(frame, event, arg):
    name = frame.f_code.co_name
    locals = frame.f_locals
    if event == "return":
        print("function: {} , locals: {} ".format(name, locals))
    return tracefunc


def foo():
    a = 12
    b = 21
    return a + b

sys.settrace(tracefunc)
foo()
