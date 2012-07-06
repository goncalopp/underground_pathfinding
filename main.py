from graph import GraphVertex, UndirectedGraphEdge

#read station names
station_names= open('station_names.txt').read().split("\n")
#create dictionary with station names as keys and vertices as values
stations= dict( [(name, GraphVertex(name)) for name in station_names] )


#read edges from file
for line in open('tube_edges.txt').read().split("\n"):
    if line!="":    #ignore empty lines
        line=line[1:-1] #strip parentheses
        station1, station2, line_name= line.split(", ") #note the whitespace
        #get the station vertices
        try:
            v1,v2= stations[station1], stations[station2]
            #we need to check if there's no vertex connecting v1 and v2
            #already, since tube_edges returns DIRECTED edges, thus
            #listing a (assumedly undirected) edge twice
            if not v2 in v1.adjacencyList(): 
                #using the adjacencyList for checking this is  
                #ineficient. A much better solution would involve 
                #storing a dictionary of all processed tuples of (v1,v2)
                edge= UndirectedGraphEdge(v1,v2)
                #dynamically add the "line" attribute to the edge object
                edge.line= line_name
        except KeyError as e:
            print "ignoring edge to unknown station:", e.message

if __name__=='__main__':
    #example
    wm= stations['Westminster']
    print "from Westminster, we can go to:", ", ".join([s.name for s in wm.adjacencyList()])
