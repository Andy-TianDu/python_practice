__author__ = 'tian.du'


class Greeter(object):

    def __init__(self, user_name):
        self.name = user_name

    def say_hello(self):
        print("Hello " + self.name)

    def say_goodbye(self):
        print("See you next time " + self.name)

def run_it():
    g = Greeter("Tian Du")
    g.say_hello()
    g.say_goodbye()

if __name__ == "__main__":
    run_it()
