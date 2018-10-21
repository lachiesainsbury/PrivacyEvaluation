# If you don't have the anytree module installed, open cmd/bash/shell
# and run the command: pip install anytree
from anytree import Node, RenderTree


root = Node("*")

def buildHierarchy(x):
    for row in x:
        node = newTree(row, 0)
        printHierarchy(node.root)


# Recursively creates a tree structure from a provided hierarchy string,
# and returns the root node of the tree.
def newTree(x, index):
    if len(x) > index:
        node = Node(x[index], parent=newTree(x, index+1))
        return node
    else:
        return None


# Combines two given trees based upon common elements to produce a tree
# with unique elements only. The root of the merged tree is returned.
def merge(tree1, tree2):
    return tree1


# Given a root node and a node name, recursively searches for a node in
# the tree which matches the node name.
def findNode(node, nodeName):
    if node.name == nodeName:
        return node
    else:
        for child in node.children:
            return findNode(child, nodeName)

    return None


# Prints a hierarchy in a readable format.
def printHierarchy(node):
    for pre, fill, node in RenderTree(node):
        print("%s%s" % (pre, node.name))