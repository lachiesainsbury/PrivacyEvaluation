import privacy.novelEntropy as entropy
import scanner
from privacy import util
import matplotlib.pyplot as plt
import glob
from privacy import KLDivergence

datasets = ["../data/adult/income-values/adult.csv", "../data/adult/income-values/2-anonymised.csv",
            "../data/adult/income-values/5-anonymised.csv", "../data/adult/income-values/10-anonymised.csv",
            "../data/adult/income-values/25-anonymised.csv", "../data/adult/income-values/50-anonymised.csv",
            "../data/adult/income-values/75-anonymised.csv", "../data/adult/income-values/100-anonymised.csv",
            ]
#datasets = glob.glob("../data/bike-sharing/*.csv")
kvalues = [1, 2, 5, 10, 25, 50, 75, 100]


def entropyGraph():

    entropies = []

    for file in datasets:
        x, y = scanner.readData(file)
        prob = util.probabilities(x)
        kEntropy = []
        for i in prob:
            p = list(i.values())
            kEntropy.append(entropy.entropy(p))
        entropies.append(kEntropy)
    # for i in entropies:
    #     print("#####################")
    #     for j in i:
    #         print(j)
    newE = [list(i) for i in zip(*entropies)]

    names = ["Age", "Workclass", "Education", "Marital Status", "Occupation", "Race", "Sex", "Country"]
    names = ["Season", "Year", "Month", "hour", "Holiday", "weekday", "working day", "weather", "temperature", "feeling temperate", "humidity", "wind speed"]
    graph = 6
    plt.plot(kvalues, newE[graph], linestyle='--', marker='o')
    #plt.plot(kvalues, newE[7], linestyle='--', marker='o')
    plt.title("Entropy: Bike Sharing ("+names[graph]+")")
    #plt.legend([names[0],names[7]], loc='lower right')
    plt.xlabel("K Value")
    plt.ylabel("Entropy")
    plt.show()

def klGraph():

    kl = []

    for file in datasets:
        x, y = scanner.readData(file)
        kl.append(KLDivergence.KL(x))
    plt.plot(kvalues, kl, linestyle='--', marker='o')
    plt.title("KL-Divergence: Adult")
    plt.xlabel("K Value")
    plt.ylabel("KL-Divergence")
    plt.show()

if __name__ == "__main__":
    klGraph()