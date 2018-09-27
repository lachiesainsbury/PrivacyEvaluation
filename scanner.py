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

def readDataAsInts(filename):
    with open(filename, 'r') as f:
        x = []
        y = []

        reader = csv.reader(f)
        values = [{} for i in range(len(reader[0]))]
        for row in reader:
            for i in row:
                if row[i] not in values[i]:
                    values[i][row[i]] = len(values[i])
                row[i] = values[i[row[i]]]
            x.append(row[:-1])
            y.append(row[-1])

    return x,y