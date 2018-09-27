import csv

def readData(filename):

    with open(filename, 'r') as f:
        x = []
        y = []

        reader = csv.reader(f)
        for row in reader:
            x.append(row[:-1])
            y.append(row[-1])

    return x,y

