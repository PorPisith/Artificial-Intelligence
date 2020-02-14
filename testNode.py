from Node import *

goal = Node([0, 1, 2, 3]) # Goal node
root = Node([0, 0, 0, 0]) # Create a root node
depth = goal.getSize() # depth of tree
branchingFactor = pow(2, depth) # branching factor of each node

for i in range(0, branchingFactor):
    root.addBranch(Node([0, 0, 0, i]))

for i in range(0, root.getBranchSize()):
    for j in range(0, branchingFactor):
        root.branch[j].addBranch(Node([0, 0, j, i]))

for i in range(0, root.getBranchSize()):
    for j in range(0, root.branch[i].getBranchSize()):
        for k in range(0, branchingFactor):
            root.branch[i].branch[j].addBranch(Node([0, i, j, k]))

for i in range(0, root.getBranchSize()):
    for j in range(0, root.branch[i].getBranchSize()):
        for k in range(0, root.branch[i].branch[j].getBranchSize()):
            for m in range(0, branchingFactor):
                root.branch[i].branch[j].branch[k].addBranch(Node([i, j, k, m]))

print(root.branch[10].branch[5].branch[15].getData())