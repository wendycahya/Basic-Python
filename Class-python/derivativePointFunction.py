def f(x):
    return x ** 2


def df_dx(x):
    dx = 0.000001
    return (f(x + dx / 2) - f(x - dx / 2)) / dx


for x in range(10):
    print(x, f(x), df_dx(x)) 