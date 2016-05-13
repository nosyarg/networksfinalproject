import random
n = int(input("Enter number of vertices: "))
p = float(input("Enter edge probability: "))
writefile = open("erdosgraph.txt","w")
graph = []
for i in range(0,n):
        for j in range(i+1,n):
                if (random.random() < p):
                        graph.append((i,j))
writefile.write(str(graph))
