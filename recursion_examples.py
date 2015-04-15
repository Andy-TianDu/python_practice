__author__ = 'tian.du'


def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


if __name__ == "__main__":
    print(mysum([1, 2, 3, 4, 5]))
