import matplotlib.pyplot as plt
import timeit
import functools


def del_(target):
    del target


plt_x = []
plt_l = []
plt_d = []

for i in range(100):
    lst = [k for k in range(i)]
    dct = {}
    for j in lst:
        dct.update({j: j})
    t_lst = timeit.Timer(functools.partial(del_, lst)).timeit()
    t_dct = timeit.Timer(functools.partial(del_, dct)).timeit()
    plt_x.append(i)
    plt_l.append(t_lst)
    plt_d.append(t_dct)

plt.plot(plt_x, plt_l)
plt.plot(plt_x, plt_d)
plt.show()

