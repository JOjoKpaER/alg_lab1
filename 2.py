import matplotlib.pyplot as plt
import timeit
import functools


def v1(lst):
    for i in range(len(lst)):
        if lst[i] in lst[i+1:None]:
            return False
    return True


def v2(lst):
    st = set(lst)
    if len(st) == len(lst):
        return True
    return False


plt_x = []
plt_v1 = []
plt_v2 = []

for i in range(10):
    lst = [j for j in range(i)]
    t_v1 = timeit.Timer(functools.partial(v1, lst)).timeit()
    t_v2 = timeit.Timer(functools.partial(v2, lst)).timeit()
    print(t_v1, t_v2)
    plt_x.append(i)
    plt_v1.append(t_v1)
    plt_v2.append(t_v2)

plt.plot(plt_x, plt_v1)
plt.plot(plt_x, plt_v2)
plt.show()
