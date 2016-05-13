path = input("enter file path: ")
graph = []
with open(path) as readfile:
    for line in readfile:
            temparr = line.split(' ')
            graph.append((int(temparr[0]),int(temparr[1])))
components = []
while (graph != []):
        currentcomp = []
