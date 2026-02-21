def myfunc(x):
    return lambda a: a**x
first=myfunc(3)
print(first(2))