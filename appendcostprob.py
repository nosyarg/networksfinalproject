import random
def probdist(edge): #insert probability distribution function
        return random.random()
def costdist(edge): #insert cost distribution function
        return random.random()
path = input("enter file path: ")
graph = []
with open(path) as readfile:
    for line in readfile:
        temparr = line.split(' ')
        graph.append((int(temparr[0]),int(temparr[1])))
writegraph = []
for i in graph:
       writegraph.append((i[0],i[1],probdist(i),costdist(i)))
writestr = ""
writefile = open("probcostgraph.pcn","w")
for i in writegraph:
        writestr += ' '.join(map(str,i)) + "\n"
writefile.write(writestr)
writefile.close()
