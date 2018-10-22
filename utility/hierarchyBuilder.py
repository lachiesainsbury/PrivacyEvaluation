# If you don't have the anytree module installed, open cmd/bash/shell
# and run the command: pip install anytree
from anytree import Node, RenderTree
from anytree import LevelOrderIter


# Builds a hierarchy in a tree data structure given the rows of the csv input
def buildHierarchy(x):
    root = Node("*")

    for row in x:
        tree = newTree(row, 0)
        mergeTrees(root, tree.root)

    return root



# Recursively creates a tree structure from a provided hierarchy string,
# and returns the root node of the tree.
def newTree(x, index):
    if len(x) > index:
        node = Node(x[index], parent=newTree(x, index+1))
        return node
    else:
        return None



# Merges two trees together into tree1. The nodes are merged on equivalent
# branches so that the root tree only contains unique elements.
def mergeTrees(tree1, tree2):
    # For each node in a breadth first traversal of the given tree
    for node in LevelOrderIter(tree2):
        exists = False

        # If the tree node doesn't have a parent, skip it
        if node.parent == None:
            continue

        # Otherwise, find the current nodes parent in the root tree
        found = findNode(tree1, node.parent.name)

        # Loop through each child of the found node in the root tree
        for child in found.children:
            # If a child exists which matches our current node, move onto the
            # next bfs node as we don't want duplicates
            if child.name == node.name:
                exists = True
                break

        # If we looped through every child and the node doesn't exist, then
        # set it as a child of the found node
        if exists == False:
            node.parent = found
            return



# Given a root node and a node name, recursively searches for a node in
# the tree which matches the node name.
def findNode(node, nodeName):
    if node.name == nodeName:
        return node

    for child in node.children:
        n = findNode(child, nodeName)
        if n:
            return n

    return None



# Returns the total number of nodes on the level below the given node.
def countNodesOnLevelBelow(node):
    nodeCount = len(node.children)

    for sibling in node.siblings:
        nodeCount += len(sibling.children)

    return nodeCount



# Prints a hierarchy in a readable format.
def printHierarchy(node):
    for pre, fill, node in RenderTree(node):
        print("%s%s" % (pre, node.name))