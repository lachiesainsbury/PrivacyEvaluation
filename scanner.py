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


def readHierarchy(filename):
    with open(filename, 'r') as f:
        x = []
        reader = csv.reader(f)

        for row in reader:
            x.append(row[0].split(";"))

    return x


def numberOfEquivalenceClasses(filename):
    with open(filename, 'r') as f:
        num = 0
        eq = []

        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            eq.append(row[:-1])

        for i in range(len(eq)):
            if eq[i] != eq[i - 1]:
                num = num + 1

    return num


def returnEQArray(filename):
    with open(filename, 'r') as f:
        num = []
        count = 1
        eq = []
        eq2 = []

        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            eq.append(row[:-1])

        for i in range(len(eq)):
            if (i + 1) < len(eq):
                if eq[i + 1] != eq[i]:
                    eq2.append(eq[i])
                    num.append(count)
                    count = 1
                else:
                    count = count + 1
            else:
                eq2.append(eq[i])
                num.append(count)

    return eq2, num
