_author__ = 'tian.du'


def func(a):
    a = 99


def changer(a, b):
    a = 2
    b[0] = 'spam'


if __name__ == "__main__":
    b = 88
    print(b)
    func(b)
    print(b)

    X = 1
    L = [1, 2]
    print(X, L)
    changer(X, L)
    print(X, L)
