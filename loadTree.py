from Node import *
import pickle

goal = Node([0, 1, 2, 3]) # Goal node

with open('data.tree', 'rb') as data_file:
    root = pickle.load(data_file)
    print(root.branch[10].branch[5].branch[15].getData())
    
print(goal.getData())
depth = goal.getSize()
print(depth) # depth of tree)