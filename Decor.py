import datetime

def outer(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        action = func(*args, **kwargsd)
        print(datetime.datetime.now() - start)
        return action
    return inner

@outer
def add(a, b):
    return a + b

@outer
def mult(a, b):
    return a * b

result1 = add(2, 2)
print(result1)

result2 = mult(2, 2)
print(result2)