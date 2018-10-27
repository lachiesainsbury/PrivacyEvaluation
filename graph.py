import matplotlib.pyplot as plt

def plot(x, y, title, xlabel, ylabel):
    plt.plot(x, y, linestyle='--', marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()