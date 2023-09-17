import matplotlib.pyplot as plt
import timeit
import functools


def foo(i): # i - число
    digits = "0123456789"
    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i // 10
    return result


plt_x = []
plt_foo = []
for i in range(100):
    foo_t = timeit.Timer(functools.partial(foo, i))
    plt_x.append(i)
    plt_foo.append(foo_t.timeit())
    print(i, plt_foo[-1])


plt.plot(plt_x, plt_foo)
plt.show()
