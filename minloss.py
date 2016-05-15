#Networks Final Project Main Script
#Grayson York, Luke Zeller, Matthew Zheng, Junmo Ryang
#Calculates most efficient possible path through a network in which each edge has both a cost and a failure probability associated with it.
#I will start out with pulling in the graph and storing the maximum vertex number
path = input("enter file path: ")
maxval = 0
graph = []
with open(path) as readfile:
    for line in readfile:
        temparr = line.split(' ')
        graph.append((int(temparr[0]),int(temparr[1]),float(temparr[2]),float(temparr[3])))
        if(int(temparr[0]) > maxval):
                maxval = int(temparr[0])
        elif(int(temparr[1]) > maxval):
                maxval = int(temparr[1])
graphtmp = graph[:]
#now I would like to get the starting and ending vertices
start = int(input("ENTER STARTING VERTEX: "))
end = int(input("ENTER ENDING VERTEX: "))
#now I will compute all of the degrees of vertices
degs = [0] * (maxval+1)
for i in graph:
        degs[i[0]] += 1
        degs[i[1]] += 1

# now, I will remove all degree 1 vertices which are not the starting or ending vertex
for index,val in enumerate(degs):
        if(val == 1):
                j = 0
                while(j<len(graph)):
                        current = graph[j]
                        if(current[0] == index or current[1] == index and current[1] != last and current[0] != first):
                                del graph[j]
                                j = len(graph)
                        else:
                                j+=1
#        if(val == 2):
                #reduce degree 2 vertices
print(degs)
writestr = ""
writefile = open("testnet.pcn","w")
for i in graph:
        writestr += ' '.join(map(str,i)) + "\n"
writefile.write(writestr)
writefile.close()          
