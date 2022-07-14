import time


def memoize(func):
    f_a_log = {}
    def lookup(*args):
        key = (func, args)
        if key not in f_a_log:
            f_a_log[key] = func(*args)
        return f_a_log[key]
    return lookup

def fibbonaci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibbonaci(n - 2) + fibbonaci(n - 1)

@memoize
def fibbonaci_memoize(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibbonaci_memoize(n - 2) + fibbonaci_memoize(n - 1)

n_arr = [i for i in range(10, 50, 5)]

def test_fibbonaci(n):
    nonmem_arr, mem_arr = [], []
    start_nonmemoize = time.time()
    fibbonaci(n)
    time_dif_nonmem = time.time() - start_nonmemoize
    nonmem_arr += [time_dif_nonmem]
    print(f'Non-memoized fibbonaci({n}) takes {time_dif_nonmem}')

    start_memoize = time.time()
    fibbonaci_memoize(n)
    time_dif_mem = time.time() - start_memoize
    mem_arr += [time_dif_mem]
    print(f'Memoized fibbonaci({n}) takes {time_dif_mem}')
    print('\n')
    return nonmem_arr, mem_arr

for i in n_arr:
    test_fibbonaci(i)