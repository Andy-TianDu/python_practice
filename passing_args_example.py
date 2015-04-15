__author__ = 'tian.du'

def args(a, b, c):
    print("Calling method")
    print(a, b, c)

def keyword_args(c=3, b=2, a=1):
    print("Calling method with keyword arguments")
    print(a, b, c)

def example_keyword_ars(name, age, job):
    print(name, age, job)

def default_args(id, company="Google", salary=0):
    print(id, company, salary)

def keywrod_and_default_args(spam, eggs, toast=0, ham=0):
    # First two args are required
    print(spam, eggs, toast, ham)

def f(*args):
    print(args)

def func(**args):
    print(args)

def func_with_various_args(a, *pargs, **kargs):
    print(a, pargs, kargs)

if __name__ == "__main__":
    args(1, 2, 3)

    keyword_args(1, 2, 3)
    example_keyword_ars(age=25, name="Tian Du", job="Software Engineer")

    default_args(12345)
    default_args(23412, salary=200)

    keywrod_and_default_args(1, 2)
    keywrod_and_default_args(1, ham=1, eggs=0)
    keywrod_and_default_args(spam=1, eggs=0)
    keywrod_and_default_args(toast=1, eggs=2, spam=3)
    keywrod_and_default_args(1, 2, 3, 4)

    f(1)
    f(1, 2)
    f(1, 2, 3, 4)

    func(a=1, b=2, c=3)

    func_with_various_args(1, 2, 3, x=1, y=2)
    func_with_various_args(0)
    func_with_various_args(2, x=1, y=2)
