import math
from random import randint


def equivocate(x, p):
    eps = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            eps.add(x[j] - x[i])
    eps = list(sorted(eps))
    h = {0: entropy(p)}

    # helper_h = {0: [entropy(p[i]) for i in range(len(p))]}
    helper_h = {0: [entropy(p[:i + 1]) for i in range(len(p))]}

    print("ASD", entropy(0.75) + entropy(0.15) + entropy(0.1))

    for e in range(1, len(eps)):
        helper_h[eps[e]] = [None for i in range(len(p))]
        helper_h[eps[e]][0] = 0
        helper_h[eps[e]][1] = entropy(p[0])
        for i in range(2, len(p)):
            j = i
            p_partial = 0
            helper_h[eps[e]][i] = helper_h[eps[e - 1]][i]
            while (x[i] - x[j] <= eps[e]) and j != 0:
                p_partial += p[j]
                temp_h = entropy(p_partial) + helper_h[eps[e]][j - 1]
                if temp_h < helper_h[eps[e]][i]:
                    helper_h[eps[e]][i] = temp_h
                j -= 1
        h[eps[e]] = helper_h.get(eps[e])[-1]
    return fill_dict(h)


def fill_dict(x):
    dict_range = list(range(min(x.keys()), max(x.keys()) + 1))
    filled_dict = {}
    recent = x[0]
    for fill_index in dict_range:
        if fill_index in x.keys():
            recent = x[fill_index]
        filled_dict[fill_index] = recent
    return filled_dict


def entropy(p):
    if not isinstance(p, list):
        return p * math.log(1 / p, 2)
    entropy_sum = 0
    for i in range(len(p)):
        entropy_sum += p[i] * math.log(1 / p[i], 2)
    return entropy_sum
