import csv


def readData(filename):
    with open(filename, 'r') as f:
        x = []
        y = []


        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            x.append(row[:-1])
            y.append(row[-1])

    return x, y


def readDataAsInts(filename):
    with open(filename, 'r') as f:
        x = []
        y = []

        reader = csv.reader(f)
        header = next(reader)
        values = [{} for i in range(len(header))]
        next(reader)
        for row in reader:
            for i in range(len(row)):
                if row[i] not in values[i]:
                    values[i][row[i]] = len(values[i])
                row[i] = values[i][row[i]]
            x.append(row[:-1])
            y.append(row[-1])

    return x, y


def returnNumberofRecords(filename):
    with open(filename, 'r') as f:
        z = 0

        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            z = z + 1

    return z

def numberOfEquivalenceClasses(filename):
    with open(filename, 'r') as f:
        num = 0
        eq = []

        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            eq.append(row[0])

        for i in range(len(eq)):
            if eq[i] != eq[i-1]:
                num = num + 1

    return num