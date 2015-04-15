__author__ = 'tian.du'


def basic_types():
    i = 1
    j = 2.3

    # is there char in python ?
    c = 'c'
    print(type(c))
    str = "Intro to Python"
    print(type(str))

    h = "Love "
    b = "Python~ "
    print((h + b) * 10)


def main():
    basic_types()

if __name__ == "__main__":
    main()