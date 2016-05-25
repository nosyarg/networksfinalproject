#NETWORKS FINAL PROJECT, MINIMUM COST MAXIMUM SUCCESS ROUTING OVER NETWORKS
#GRAYSON YORK, LUKE ZELLER, MATTHEW ZHENG, JUNMO RYANG
#5/25/2016
import random
numvert = 100
def maxnum(graph):
        maxval = 0
        for edge in graph:
                if edge[1] > maxval:
                        maxval = edge[1]
        return maxval
def degree(graph):
        maxval = maxnum(graph)
        #compute all of the degrees of vertices
        degs = [0] * (maxval+1)
        for edge in graph:
                degs[edge[0]] += 1
                degs[edge[1]] += 1
        return degs
def outdeg(graph):
        maxval = maxnum(graph)
        #compute all of the degrees of vertices
        degs = [0] * (maxval+1)
        for edge in graph:
                degs[edge[0]] += 1
        return degs
def indeg(graph):
        maxval = maxnum(graph)
        #compute all of the degrees of vertices
        degs = [0] * (maxval+1)
        for edge in graph:
                degs[edge[1]] += 1
        return degs
def probdist(edge): #insert probability distribution function
        return random.random()
def costdist(edge): #insert cost distribution function
        return random.random()
def graphgen():#insert graph generation function which should append the cost and probabilities
        n = numvert
        p = .1
        graph = []
        for i in range(0,n):
                for j in range(i+1,n):
                        if (random.random() < p): 
                                graph.append((i,j,probdist((i,j)),costdist((i,j))))
        return graph
def acyclic(graph):
        return graph
#this should eventually remove cycles from the graph, probably easiest to do by ensuring that all destinations are less than origins
def removezero(graph):
        degs = degree(graph)
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
def cutirrelevant(graph,exempt):
        degs = degree(graph)
        for index,val in enumerate(degs):
                if val == 1: #cut degree 1 vertices
                        j = 0 
                        while j<len(graph):
                                current = graph[j]
                                if((current[0] == index or current[1] == index) and not (current[1] in exempt or current[0] in exempt)):
                                        del graph[j]
                                        j = len(graph)
                                else:
                                        j+=1 #todo, cut out sink vertices and source vertices and simplify degree 2's
        degs = degree(graph)
        index = 0
        while(index < len(degs)):
                degs = degree(graph)
                val = degs[index]
                if val == 2: #simplify degree 2 vertices this is malfunctioning, zero has way to high of degree and there are still too many degree 2 vertices
                        j = 0
                        while j < len(graph):
                                first = graph[j]
                                if (first[1]  == index) and not (first[0] in exempt or first[1] in exempt):
                                        i = j+1
                                        while i < len(graph):
                                                second = graph[i]
                                                if (second[0] == index) and not (second[0] in exempt or second[1] in exempt):
                                                        new = (first[0],second[1],first[2]*second[2],first[3]+second[3])#make a new edge which is a combination of the other two
                                                        graph[j] = new
                                                        del graph[i]
                                                        i = len(graph)
                                                        j = len(graph)
                                                        index = len(degs)
                                                i += 1
                                j += 1
                index+=1
        hasin = [0]*len(degree(graph))
        hasout = [0]*len(degree(graph))
        for val in graph:
                hasout[val[0]] = 1 or hasout[val[0]]
                hasin[val[1]] = 1 or hasin[val[1]]
        i = 0
        while i < len(graph):
                val = graph[i]
                if (not hasin[val[0]] and not val[0] in exempt) or (not hasin[val[1]] and not val[1] in exempt):
                        del graph[i]
                else:
                        i+=1
        return graph
#BEGIN PROGRAM
writefile = open("junmofile.csv","a")
while(1):
        graph = graphgen()
#        print("GRAPH GENERATED, E = " + str(len(graph)))
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
        vertinpath = [0]
        current = 0
        for i in graph:
                        if i[0] in vertinpath and not i[1] in vertinpath:
                                vertinpath.append(i[1])
        i = 0
        while(i < len(graph)):
                current = graph[i]
                if not current[0] in vertinpath:
                        del graph[i]
                else:
                        i += 1
        graph = removezero(graph)
#        print("GC isolated, E = " + str(len(graph)))
        graphtmp = []
        while(graph != graphtmp):#get rid of all the vertices we know we wont pass through
                graphtmp = graph[:]
                start = 0
                end = maxnum(graph)
                graph = removezero(cutirrelevant(graph,[start,end]))
#        print("Irrelevant vertices cut, E = " + str(len(graph)))
        #now lets get into the code...
        n = maxnum(graph)
        #graph.sort(key = lambda x:x[1])
        probs = [1]*(n+1)
        probs[0] = 0
        for i in range(0,len(graph)):
                current = graph[i]
                probs[current[1]] *= (1 - (current[2] * (1 - float(probs[current[0]]))))
#        print("PROBABILITY: " + str(probs[-1]))
        writefile.write(str(numvert)+ "," + str(len(graph)) + "," + str(1.0 - probs[-1]) + "\n")
