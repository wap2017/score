name = "outter"


def hello():
    global name
    name = "inner"
    print('hello', name)


if __name__ == "__main__":
    hello()
    print(name)
