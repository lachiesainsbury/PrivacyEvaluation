import math


def equivocate(x, p):
    eps = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            eps.add(x[j] - x[i])
    eps = list(sorted(eps))

    h = {0: entropy(p)}

    helper_h = {0: [h[0] for i in range(len(p))]}

    for e in range(1, len(eps)):
        helper_h[eps[e]] = [0, entropy([p[0]])]
        for i in range(1, len(p)):
            j = i
            p_partial = 0
            helper_h[eps[e]].append(helper_h[eps[e - 1]][i])
            while (x[i] - x[j] <= eps[e]) and j != 0:
                p_partial += p[j]
                temp_h = entropy([p_partial]) + helper_h[eps[e]][j - 1]
                if temp_h < helper_h[eps[e]][j]:
                    helper_h[eps[e]][j] = temp_h
                j -= 1
        h[eps[e]] = helper_h[eps[e]][-1]
    return fill_dict(h)


def fill_dict(dict):
    dict_range = list(range(min(dict.keys()), max(dict.keys())))
    filled_dict = {}
    recent = dict[0]
    for fill_index in dict_range:
        if fill_index in dict.keys():
            recent = dict[fill_index]
        filled_dict[fill_index] = recent
    return filled_dict


def entropy(p):
    entropy_sum = 0
    for i in range(len(p)):
        entropy_sum += p[i] * math.log(1 / p[i], 2)
    return entropy_sum
