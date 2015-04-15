__author__ = 'tian.du'


def while_loop():
    i = 0
    while i < 5:
        i += 1
        print(i)

    counter = 0
    while True:
        print("Counter = " + str(counter))
        counter += 1

        if counter >= 10:
            break


def user_input():
    print("simple REPL (type \"q\" to quit):")
    while True:
        user_typed = input(">")
        if user_typed == "q":
            print("Good Bye")
            break
        else:
            print(user_typed)

if __name__ == "__main__":
    while_loop()
    user_input()

