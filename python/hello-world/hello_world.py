def hello(name=''):
    if name is '':
        print("Hello, World!")
    elif name is None:
        return ("Hello, World!")
    else:
        return ("Hello, %s!") % name
