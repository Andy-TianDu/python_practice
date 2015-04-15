__author__ = 'tian.du'


def dict_test():
    ice_cream = {"Alice": "chocolate", "Bob": "strawberry", "Cara": "mint chocolate chip"}
    print(ice_cream["Alice"])

    ice_cream["Eve"] = "rum raisin"
    print(ice_cream)

    print("Eve" in ice_cream)

    # create an empty dict
    phone_number = {}
    print(type(phone_number))

if __name__ == "__main__":
    dict_test()
