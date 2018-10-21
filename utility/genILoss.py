import scanner
import os
import utility.hierarchyBuilder as hb

hierarchyDirectory = "data/arx/hierarchies/"

def calcGenILoss(x, y):
    recordCount = len(x)
    attributeCount = len(x[0])

    hierarchies = []

    #for filename in os.listdir(hierarchyDirectory):
        #hierarchy = hb.buildHierarchy(scanner.readHierarchy(hierarchyDirectory + filename))
        #hierarchies.append(hierarchy)

    hb.buildHierarchy(scanner.readHierarchy(hierarchyDirectory + "maritalstatus.csv"))
