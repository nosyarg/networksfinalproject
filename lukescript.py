import random
n = int(input("n:"))
p = float(input("p:"))
def graphgen(n,p):
        graph = []
        for i in range(0,n):
                for j in range(i+1,n):
                        if (random.random() < p): 
                                graph.append((i,j))
        return graph
graph = graphgen(n,p)
vertinpath = [0]
for edge in graph:
                if edge[0] in vertinpath and not edge[1] in vertinpath:
                        vertinpath.append(edge[1])
if (n-1) in vertinpath:
        print("accessible")
else:
        print("inaccessible")
