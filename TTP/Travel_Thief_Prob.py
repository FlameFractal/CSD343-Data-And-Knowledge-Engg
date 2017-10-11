"""
Created on Tue Aug 29 19:41:17 2017

@authors:
    Samarjoy Pandit
    Saurabh Datir
    Vishal Gauba
    Saksham Rastogi
    Akanksha Jojwan
"""

# An adjacency list representation of the graph of cities
Graph = {
			1:[(2, 35), (3, 20), (4, 45), (5, 10), (6, 90), (7, 20)], 
			2:[(1, 35), (4, 40), (5, 15), (6, 20), (7, 25)], 
			3:[(1, 20), (4, 40), (6, 75)],
			4:[(1, 45), (2, 40), (3, 40), (6, 50), (7, 35)],
			5:[(1, 10), (2, 15), (6, 10)],
			6:[(1, 90), (2, 20), (3, 75), (4, 40), (5, 10)],
			7:[(1, 20), (2,25), (4, 35), (6, 45)]

		}

ItemSet = {
	
			1:[ 300, 50, (1, 2, 3, 4, 5, 6, 7)],
			2:[ 600, 25, (3, 5, 7)],
			3:[ 200, 100, (1, 2, 4, 6)],
			4:[ 100, 10, (4, 5, 6, 7)],
			5:[ 250, 75, (1, 2, 3)]
}

# We maintain global variables to maintain our state during graph traversal for shortest path calculation
Visited = [0]*len(Graph)
ShortestPath = []
PathLen = []
VMax = 20
VMin = 10
R = 0.1
W = 600

def GetPath(index):
    
    global Graph, Visited, PathLen, ShortestPath
    
    ShortestPath = ShortestPath + [index,]
    
    if Visited != [1]*len(Graph):
        Visited[index-1] = 1
        min = float("inf")
        small = ()
        
        # find the unvisited city with minimum distance for ith node in the graph and recursively call path() on that node
        for e in Graph[index]:
            if Visited[e[0] - 1] == 0 and e[1] < min:
                small = e
        
        if small != ():
            GetPath(small[0])
            PathLen = PathLen + [small[1]+ (PathLen[-1] if len(PathLen) > 0 else 0) , ]
        # else if all cities from the ith node are visited, then check if we can return to node 1 from the ith node
        else:
            if ShortestPath[0] in [E[0] for E in Graph[index]]:
                ShortestPath = ShortestPath + [ShortestPath[0],]
                for E in Graph[index]:
                    if E[0] == ShortestPath[0]:
                        PathLen = PathLen + [E[1] + (PathLen[-1] if len(PathLen) > 0 else 0), ]
            return
    else:
        return

for j in range(1, len(Graph) + 1):
    GetPath(j)
    # if the thief returns to his origin city then break
    if ShortestPath[0] == ShortestPath[-1]:
        break

# CityDistance contains the distance of the ith city along the path from the end of the circuit
CityDistance = [PathLen[-1] + PathLen[0] - c for c in PathLen]
ThiefBag = []
# Time is calculated assuming average velocity throughout the tour.
Time = 2*PathLen[-1]*(VMax + VMin)

for item,value in ItemSet.items():
    for k in value[2]:
        # Here 'k' is the cities in which the item is present
        profit = int(value[0] - (0.25*value[0]*(CityDistance[ShortestPath.index(k)]/PathLen[-1])) - (R*Time*value[1]/W))
        ThiefBag = ThiefBag + [[item, k, value[1], profit, value[0]],]

#We sort the items by their profit, and then keep picking till the knapsack's weight limit is reached
ThiefBag.sort(key = lambda x: int(x[3]))
# Here, we need the items sorted descending by their heuristic profit
ThiefBag.reverse()

c = 0
i = 0
ItemsPicked = []
TotalProfit = 0

# Calculating total profit based on the items picked by the thief
while i < len(ThiefBag):
    if c + ThiefBag[i][2] <= W:
        ItemsPicked = ItemsPicked + [[ThiefBag[i][0], ThiefBag[i][1]],]
        c = c + ThiefBag[i][2]
        TotalProfit = TotalProfit + ThiefBag[i][4]
    
    i = i + 1

ItemsPicked.sort(key = lambda x: int(x[0]))
values = sorted(set(map(lambda x:x[0], ItemsPicked)))

Arr = []

for i in values:
    templist = []
    for j in ItemsPicked:
        if j[0] == i:
            templist = templist + [j[1],]
    
    templist.sort()
    Arr = Arr + [[i, templist],]

print()
print("Path taken by thief: " + str(ShortestPath))
print("Distance covered: " + str(PathLen[-1]))
print("Items picked: ")
for i in Arr:
    print("\tCity: " + str(i[0]) + "\t\tItems: " + ', '.join(str(e) for e in i[1]))

print("Total Weight: " + str(c))
print("Total Profit: " + str(TotalProfit))