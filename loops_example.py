__author__ = 'tian.du'


def loops():
    names = ["Alice", "Bob", "Cassie", "Diane", "Ellen"]

    for name in names:
        print(name)

    for word in names:
        print("Hello " + word)

    for name in names:
        if name[0] in "AEIOU":
            print(name + " starts with a vowel")

    # build up a list
    vowel_names = []
    for name in names:
        if name[0] in "AEIOU":
            vowel_names.append(name)
    print(vowel_names)


def add_up():
    prices = [1.5, 2.35, 5.99, 16.49]
    total = 0
    for price in prices:
        total += price
    print("Total is:")
    print(total)
    print("You could also use the sum() function")
    print(sum(prices))

if __name__ == "__main__":
    loops()
    add_up()