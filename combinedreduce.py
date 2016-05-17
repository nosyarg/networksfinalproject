import random
def probdist(edge): #insert probability distribution function
        return random.random()
def costdist(edge): #insert cost distribution function
        return random.random()
def graphgen():#insert graph generation function which should append the cost and probabilities
        n = 1000
        p = .01
        graph = []
        for i in range(0,n):
                for j in range(i+1,n):
                        if (random.random() < p): 
                                graph.append((i,j,probdist((i,j)),costdist((i,j))))
        return graph
#def acyclic(graph):
#this should remove cycles from the graph, probably easiest to do by ensuring that all destinations are less than origins
def removezero(graph):
#now I will compute all of the degrees of vertices
        maxval = 0
        for edge in graph:
                if edge[1] > maxval:
                        maxval = edge[1]
        degs = [0] * (maxval+1)
        for edge in graph:
                degs[edge[0]] += 1
                degs[edge[1]] += 1
        #now go through the degrees, and rewire to lower numbers when zero 
        newindices = {}
        zerodegs = []
        for index,val in enumerate(degs):#create a dictionary mapping current locations to desired new locations
                if val == 0:
                        zerodegs.append(index)
                elif len(zerodegs) == 0:
                        newindices[index] = index
                else:
                        newindices[index] = zerodegs.pop(0)
                        zerodegs.append(index)
        for index,edge in enumerate(graph):
                graph[index] = (newindices[edge[0]],newindices[edge[1]],edge[2],edge[3])
        return graph
        #this function should reduce the graph to remove disconnected edges 
graph = graphgen()
print("GRAPH GENERATED, E = " + str(len(graph)))
graphtmp = graph[:]
components = []
currentcomponent = []
while(len(graphtmp) != 0):#this will loop over all the edges in graphtmp to cut out anything not in the GC 
        index = 0 
        currentcomponent.append(graphtmp[0][0]) #set current head vertex
        currentcomponenttmp = currentcomponent[:] #create a snapshot of the current component for the purpose of checking if new things are added
        while(index < len(currentcomponent) and currentcomponenttmp == currentcomponent):
                if(currentcomponenttmp != currentcomponent and index >= len(currentcomponen)):
                        index = 0  #reset the index when we add a new vertex, there is probably a faster way to do this, but this works relatively quickly
                i = 0 
                currentcomponenttmp = currentcomponent[:]
                while(i < len(graphtmp)):
                        currentedge = graphtmp[i]#figure out whether the edge is in the current component and if not add it and dispose of it from the main graph.
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
for i in components:#find the length of each component
        lens.append(len(i))
gc = components[lens.index(max(lens))]#only take the component with the maximum length
i = 0;
while(i < len(graph)):#delete all vertices not in the gc
        currentedge = graph[i]
        if( not (currentedge[0] in gc or currentedge[1] in gc)):
                del graph[i]
        else:
                i+=1
graph = removezero(graph)
print("GC isolated, E = " + str(len(graph)))

