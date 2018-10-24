import math


def equivocate(x, p):
    eps = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            eps.add(x[j] - x[i])
    eps = list(sorted(eps))

    h = {0: entropy(p)}

    helper_h = {0: [h[0] for i in range(len(p))]}

    for e in range(1, len(eps) - 1):
        helper_h[eps[e]] = [0]
        helper_h[eps[e]].append(entropy([p[0]]))
        for i in range(1, len(p) - 1):
            p_partial = p[i]
            j = i
            helper_h[eps[e]].append(helper_h[eps[e - 1]][i])
            while (x[i] - x[j] <= eps[e]) and j != 0:
                p_partial += p[j]
                temp_h = helper_h[eps[e]][j - 1] + entropy([p_partial])
                if temp_h < helper_h[eps[e]][j]:
                    helper_h[eps[e]][j] = temp_h
                j -= 1
        print(helper_h[eps[e]])
        h[eps[e]] = helper_h[eps[e]][-1]
    return h


def entropy(p):
    entropy_sum = 0
    for i in range(len(p)):
        entropy_sum += p[i] * math.log(1 / p[i], 2)
    return entropy_sum
