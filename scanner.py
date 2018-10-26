import csv
from random import randint

import pandas


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


def generateSalaries(x, y):
    occupations = getColumn(x, 4)
    for i in range(len(x)):
        x[i].append(getSalary(occupations))

    with open("data\AdultActualValue.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in x:
            writer.writerow(line)


def getColumn(x, i):
    return [row[i] for row in x]


def getSalary(occupation):
    if occupation == "Tech-support":
        return randint(33, 53)
    elif occupation == "Craft-repair":
        return randint(25, 45)
    elif occupation == "Other-service":
        return randint(41, 61)
    elif occupation == "Sales":
        return randint(42, 62)
    elif occupation == "Exec-managerial":
        return randint(67, 87)
    elif occupation == "Prof-specialty":
        return randint(56, 76)
    elif occupation == "Handlers-cleaners":
        return randint(20, 40)
    elif occupation == "Machine-op-inspct":
        return randint(32, 52)
    elif occupation == "Adm-clerical":
        return randint(28, 48)
    elif occupation == "Farming-fishing":
        return randint(39, 59)
    elif occupation == "Transport-moving":
        return randint(41, 61)
    elif occupation == "Priv-house-serv":
        return randint(16, 36)
    elif occupation == "Protective-serv":
        return randint(59, 79)
    elif occupation == "Armed-Forces":
        return randint(34, 54)
    elif occupation == "Technical":
        return randint(35, 66)
    elif occupation == "Other":
        return randint(26, 69)
    elif occupation == "Non-technical":
        return randint(30, 77)
    else:
        return randint(26, 77)
