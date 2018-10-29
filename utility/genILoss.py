import scanner
import os
import math
import utility.hierarchyBuilder as hb


hierarchies = []

def calcGenILoss(x, hierarchyDirectory):
    hierarchies.clear()
    # Number of records in the dataset
    recordCount = len(x)

    #Number of attributes in the dataset
    attributeCount = len(x[0])

    # Build tree data structures for each csv hierarchy file
    buildHierarchies(hierarchyDirectory)

    # Tracks the cumulative loss value of each cell in the dataset
    loss = 0

    for i in range(attributeCount):
        hierarchy = hierarchies[i]

        for j in range(recordCount):
            # Find the node at x[j][i] in the current attributes hierarchy
            node = hb.findNode(hierarchy, x[j][i])

            # If the node has no children, loss = 0, so just skip it
            if not node.children:
                continue
            else:
                # Calculates the number of generalized nodes
                generalizedInterval = len(node.children) - 1
                # Calculates the total number of nodes at one level lower in the hierarchy
                attributeInterval = hb.countNodesOnLevelBelow(node) - 1

                loss += generalizedInterval / attributeInterval

    # Normalise the loss value to within a range of 0 - 1
    loss *= (1/ (attributeCount * recordCount))

    return loss


# Builds a hierarchy for each csv file within the hierarchyDirectory
def buildHierarchies(hierarchyDirectory):
    for filename in os.listdir(hierarchyDirectory):
        hierarchy = hb.buildHierarchy(scanner.readHierarchy(hierarchyDirectory + filename))
        hierarchies.append(hierarchy)