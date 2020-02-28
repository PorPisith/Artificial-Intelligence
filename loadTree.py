from Node import *
import pickle
from collections import deque 

goal = Node([2,0]) # Goal node
max_depth = len(goal.data)+1
limit = 0

print("Max Depth = ",max_depth," Limit = ",limit)

with open('data.tree', 'rb') as data_file:
    root = pickle.load(data_file)

depth = goal.getSize() # depth of tree
branchingFactor = pow(2, depth) # branching factor of each node

depth_search = []

def depthFirstSearch(root,max_depth): 
    Stack = deque([])  
    Preorder = [] # contains visit node
    Preorder.append(root.data) 
    Stack.append(root) 
    found = 0
    level = 0
    
    if(max_depth <= 0): # if max_depth = 0
        return print(*Preorder, sep = " > ") 
    
    while len(Stack)>0 and found == 0: 
        flag = 0
        if len((Stack[-1]).branch) == 0: # no branch
            Stack.pop() 
        else: 
            Par = Stack[-1] # node has branch
            
        for i in range(0, len(Par.branch)): 
            if Par.branch[i].data not in Preorder: 
                flag = 1
                Stack.append(Par.branch[i]) 
                Preorder.append(Par.branch[i].data) 
                # Search
                if(Par.branch[i].data == goal.data):
                    found = 1
                break; 
        if flag == 0: 
            Stack.pop() # not found remove from stack
            
    print(*Preorder, sep = " > ") 
    
def iterativeDeepeningDepthFirstSearch(root):
    for i in range (0,max_depth):
        depthFirstSearch(root,i)
        
iterativeDeepeningDepthFirstSearch(root)