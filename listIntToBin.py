goal = [2, 9, 14, 9]
searchGoal = []
for i in goal:
    searchGoal.append([int(x) for x in list('{0:04b}'.format(i))])
    
print(searchGoal)