from Node import *
import pickle
import time
import json
import jsonpickle

root = Node([0, 0, 0, 0]) # Create a root node
depth = root.getSize() # depth of tree
branchingFactor = pow(2, depth) # branching factor of each node

for i in range(0, branchingFactor):
    root.addBranch(Node([0, 0, 0, i]))

for i in range(0, root.getBranchSize()):
    for j in range(0, branchingFactor):
        root.branch[i].addBranch(Node([0, 0, j, i]))

for i in range(0, root.getBranchSize()):
    for j in range(0, root.branch[i].getBranchSize()):
        for k in range(0, branchingFactor):
            root.branch[i].branch[j].addBranch(Node([0, k, j, i]))
            
for i in range(0, root.getBranchSize()):
    for j in range(0, root.branch[i].getBranchSize()):
        for k in range(0, root.branch[i].branch[j].getBranchSize()):
            for l in range(0, branchingFactor):
                root.branch[i].branch[j].branch[k].addBranch(Node([l, k, j, i]))
       
# for i in range(0, branchingFactor):
#     root.addBranch(Node([0, 0, 0, 0, i]))

# for i in range(0, root.getBranchSize()):
#     for j in range(0, branchingFactor):
#         root.branch[j].addBranch(Node([0, 0, 0, j, i]))

# for i in range(0, root.getBranchSize()):
#     for j in range(0, root.branch[i].getBranchSize()):
#         for k in range(0, branchingFactor):
#             root.branch[i].branch[j].addBranch(Node([0, 0, i, j, k]))
            
# for i in range(0, root.getBranchSize()):
#     for j in range(0, root.branch[i].getBranchSize()):
#         for k in range(0, root.branch[i].branch[j].getBranchSize()):
#             for l in range(0, branchingFactor):
#                 root.branch[i].branch[j].branch[k].addBranch(Node([0, i, j, k, l]))
                                                             
# for i in range(0, root.getBranchSize()):
#     for j in range(0, root.branch[i].getBranchSize()):
#         for k in range(0, root.branch[i].branch[j].getBranchSize()):
#             for l in range(0, root.branch[i].branch[j].branch[k].getBranchSize()):
#                 for m in range(0, branchingFactor):
#                     root.branch[i].branch[j].branch[k].branch[l].addBranch(Node([i, j, k, l, m]))

with open('data-4d.tree', 'wb') as data_file:
    pickle.dump(root, data_file, protocol=-1)

# serialized = jsonpickle.encode(root)
# with open('data-5d.json', 'w') as outfile:
#     json.dump(serialized, outfile)
# stop_time = time.time()
# print("Create time",stop_time - start_time)

# start_time = time.time()
# with open('data-4d.tree', 'rb') as data_file:
#     root1 = pickle.load(data_file)
# stop_time = time.time()
# print("Pickle",stop_time - start_time)   
# print(root1.branch[15].branch[15].branch[15].getData())


# start_time = time.time()
# with open('data-4d.json') as json_file:
#     serialized = json.load(json_file)

# root2 = jsonpickle.decode(serialized)
# stop_time = time.time()
# print("JSON Pickle",stop_time - start_time)
# print(root2.branch[15].branch[15].branch[15].getData())

# with open('data-2d.tree', 'rb') as data_file:
#     root = pickle.load(data_file)
    
# # print(root.branch[3].getData())

# print(*root.getBranch(), sep = "\n")
print('-',root.getData())
for i in root.getBranch():
    print('--',i.getData())
    for j in i.getBranch():
        print('---', j.getData())
        for k in j.getBranch():
            print('----', k.getData())
        #     for l in k.getBranch():
        #         print('-----', l.getData())