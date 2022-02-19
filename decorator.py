def greet(fun):
    def wrapper(name):
        print('hello')
        fun(name)
        print('goodbye')

    return wrapper


@greet
def sayName(name):
    print(name)

sayName('Su Su');