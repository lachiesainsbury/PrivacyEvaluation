import math
import time

import matplotlib.pyplot as plt

from privacy import util


def equivalence_equivocate(equiv_class_values_dict):
    equivalence_class_probability = {}
    print("# equivalence classes :", len(equiv_class_values_dict.keys()))
    equivalence_class_total = 0

    # real bad way of counting rows
    for equiv_class in equiv_class_values_dict:
        equivalence_class_total += len(equiv_class_values_dict[equiv_class])

    for equiv_class in equiv_class_values_dict:
        equivalence_class_probability[equiv_class] = len(equiv_class_values_dict[equiv_class]) / equivalence_class_total

    equivocation_sum = 0
    for equiv_class in equiv_class_values_dict:
        prob = util.probabibilityDict(equiv_class_values_dict[equiv_class])
        equiv = equivocate(list(prob.keys()), list(prob.values()))
        equivocation_sum += equivalence_class_probability[equiv_class] * sum(list(equiv.values()))
    print("H(ε) area :", equivocation_sum)

    eps_length = []
    for equiv_class in equiv_class_values_dict:
        prob = util.probabibilityDict(equiv_class_values_dict[equiv_class])
        eps_length.append(len(find_eps(list(prob.keys()))))

    return


def equivocate(x, p):
    eps = find_eps(x)

    # Calculate shannon's entropy
    h = {0: entropy(p)}

    # Helper_H[e][i] represents H(e, i)
    helper_h = {0: [h[0] for i in range(len(p) + 1)]}

    for e in range(1, len(eps)):
        # Initialise the array. The first two subproblems are always going to be the same
        helper_h[eps[e]] = [None for i in range(len(p) + 1)]
        helper_h[eps[e]][0] = 0
        helper_h[eps[e]][1] = entropy(p[0])
        for i in range(1, len(p) + 1):
            j = i
            p_partial = 0
            helper_h[eps[e]][i] = helper_h[eps[e - 1]][i]
            # As these indexes are now being used to reference the array values we have to -1
            # Each new subproblem introduces one new value, we check to see if the new value introduces any new ranges,
            # and check if the new range produces a smaller entropy
            while (x[i - 1] - x[j - 1] <= eps[e]) and j != 0:
                p_partial += p[j - 1]
                temp_h = entropy(p_partial) + helper_h[eps[e]][j - 1]
                if temp_h < helper_h[eps[e]][i]:
                    helper_h[eps[e]][i] = temp_h
                j -= 1
        h[eps[e]] = helper_h.get(eps[e])[-1]
    return fill_dict(h)


def fill_dict(x):
    # Not strictly necessary for graphing, but makes area calculation easy (Just sum these values)
    dict_range = list(range(min(x.keys()), max(x.keys()) + 1))
    filled_dict = {}
    recent = x[0]
    for fill_index in dict_range:
        if fill_index in x.keys():
            recent = x[fill_index]
        filled_dict[fill_index] = recent
    return filled_dict


def find_eps(x):
    eps = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            eps.add(x[j] - x[i])
    return list(sorted(eps))


def entropy(p):
    if not isinstance(p, list):
        return p * math.log(1 / p, 2)
    entropy_sum = 0
    for i in range(len(p)):
        entropy_sum += p[i] * math.log(1 / p[i], 2)
    return entropy_sum


def export_attribute_equivocation_graph(name, attribute, output):
    start_time = time.time()
    probabilities = util.probabibilityDict(attribute)
    item = []
    item_prob = []
    for tup in sorted(probabilities):
        item.append(tup)
        item_prob.append(probabilities[tup])
    equiv = equivocate(item, item_prob)

    plt.step(list(equiv.keys()), list(equiv.values()), where="post")
    plt.fill_between(list(equiv.keys()), list(equiv.values()), step="post", alpha="0.1")
    plt.grid(True, linestyle="--", color="0.5")
    plt.xlabel("ε")
    plt.ylabel("H(ε)")
    plt.figtext(0.7, 0.9, "Area = {:0.2f}".format(sum(equiv.values())), backgroundcolor="white")
    print("{}.svg".format(name))
    plt.savefig("{}_{}.png".format(output, name))
    plt.clf()
