import matplotlib.pyplot as plt

# Plots a single function
def plot(x, y, title, xlabel, ylabel):
    plt.plot(x, y, linestyle='--', marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


# Plots two functions for Adult and Bike Sharing data sets
def plotTwo(x, y1, y2, title, xlabel, ylabel):
    plt.plot(x, y1, linestyle='--', marker='o')
    plt.plot(x, y2, linestyle='--', marker='o')
    plt.title(title)
    plt.legend(['Adult', 'Bike Sharing'], loc='lower right')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()