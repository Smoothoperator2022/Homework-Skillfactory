import numpy as np

def get_unique_loto(num):
    sample = np.arange(1, 101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample, replace=False, size=(5, 5)))
    res = np.array(res)
    return res

get_unique_loto(2)

 