import matplotlib.pyplot as plt
import timeit
import functools


def search_in_array(arr):
    return "str" in arr


def search_in_m(m):
    return "str" in m


plt_x = []
plt_arr = []
plt_m = []
for n in range(100):
    arr = list(range(n))
    m = set(range(n))
    arr_t = timeit.Timer(functools.partial(search_in_array, arr))
    m_t = timeit.Timer(functools.partial(search_in_m, m))
    plt_x.append(n)
    plt_arr.append(arr_t.timeit())
    plt_m.append(m_t.timeit())
    print("For n =", n, "Array:", "%.4f" % arr_t.timeit(), "List:", "%.4f" % m_t.timeit())

plt.plot(plt_x, plt_arr, plt_x, plt_m)
plt.show()