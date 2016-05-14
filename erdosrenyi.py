import random
n = int(input("Enter number of vertices: "))
p = float(input("Enter edge probability: "))
writefile = open("erdosgraph.nwk","w")
graph = []
for i in range(0,n):
        for j in range(i+1,n):
                if (random.random() < p):
                        graph.append((i,j))
writestr = ""
for i in range(len(graph)):
        writestr += ' '.join(map(str,(graph[i]))) + "\n"
writefile.write(writestr)
