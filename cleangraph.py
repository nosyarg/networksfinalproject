path = input("enter file path: ")
graph = []
with open(path) as readfile:
    for line in readfile:
            temparr = line.split(' ')
            graph.append((int(temparr[0]),int(temparr[1])))
graphtmp = graph[:]
components = []
currentcomponent = []
while(len(graphtmp) != 0):
        index = 0
        currentcomponent.append(graphtmp[0][0])
        currentcomponenttmp = currentcomponent[:]
        while(index < len(currentcomponent) and currentcomponenttmp == currentcomponent):
                if(currentcomponenttmp != currentcomponent and index >= len(currentcomponen)):
                        index = 0
                i = 0
                currentcomponenttmp = currentcomponent[:]
                while(i < len(graphtmp)):
                        currentedge = graphtmp[i]
                        if(currentedge[0] == currentcomponent[index] and not currentedge[1] in currentcomponent):
                                currentcomponent.append(currentedge[1])
                                del graphtmp[i]
                        elif(currentedge[1] == currentcomponent[index] and not currentedge[0] in currentcomponent):
                                currentcomponent.append(currentedge[0])
                                del graphtmp[i]
                        elif(currentedge[0] in currentcomponent and currentedge[1] in currentcomponent):
                                del graphtmp[i]
                        else:
                                i += 1
                index += 1
        components.append(sorted(currentcomponent[:]))
        currentcomponent = []
lens = []
for i in components:
        lens.append(len(i))
gc = components[lens.index(max(lens))]
i = 0;
while(i < len(graph)):
        currentedge = graph[i]
        if( not (currentedge[0] in gc or currentedge[1] in gc)):
                del graph[i]
        else:
                i+=1
writestr = ""
writefile = open("cleanedgraph.nwk","w")
for i in range(len(graph)):
        writestr += ' '.join(map(str,(graph[i]))) + "\n"
writefile.write(writestr)
writefile.close()
