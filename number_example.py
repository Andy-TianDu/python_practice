__author__ = 'tian.du'


def number_example():
    # get the number of digits of a really large number
    print("This will take time")
    print("Get the length of 2 to the square of 1000000")
    length = len(str(2 ** 1000000))
    print(length)

    print("""----- END ------""")


if __name__ == "__main__":
    number_example()
