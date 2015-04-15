__author__ = 'tian.du'


def if_else():

    if "O" in "Hello":
        print("True")
    elif "H" not in "ello World":
        print("True in elif")
    else:
        print("else")


def switch_stat(c):
    if c == 0:
        print("n == 0")
    elif c == 1 or c == 2 or c == 3:
        print("n < 4")
    else:
        print("miss a target")


def main():
    if_else()
    switch_stat(3)

if __name__ == '__main__':
    main()