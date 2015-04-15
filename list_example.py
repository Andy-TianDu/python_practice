__author__ = 'tian.du'


def test_list():
    your_list = ["a", "b", "c", "d", "e", "f"]
    print(type(your_list))

    print("Let us try slicing")
    print(your_list[1:3])

    if "a" in your_list:
        print(" a , in the list")
    elif "d" in your_list:
        print("Not in the list")

    # get one element
    print(your_list[0])
    # adding element
    your_list.append(1)
    # replace an element
    your_list[0] = "d"

    for e in your_list:
        print(e)
    # removing element

    print(len(your_list))

    # get the last element
    print(your_list[-1])
    print(your_list[len(your_list) - 1])


if __name__ == "__main__":
    test_list()