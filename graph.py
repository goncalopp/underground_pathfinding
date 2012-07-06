class GraphEdge( object ):
    '''abstract class'''
    def connection( self, vertex_a ):
        '''Returns the vertex that vertex_a is connected to by this edge (or None)'''
        raise NotImplementedError()


class GraphVertex( object ):
    '''A vertex of a graph'''
    def __init__(self, name):
        self.name= name
        self.edges= []

    def addEdge(self, edge):
        assert isinstance(edge, GraphEdge)
        self.edges.append( edge )
    
    def adjacencyList(self):
        '''returns all the vertices adjacent to this one'''
        connections= [e.connection(self) for e in self.edges]
        return filter( lambda x: not x is None, connections)

    def __repr__(self):
        return "V"+"<"+self.name+">"

class UndirectedGraphEdge( GraphEdge ):
    def __init__( self, vertex1, vertex2):
        v1,v2= vertex1, vertex2
        v1.addEdge(self)
        v2.addEdge(self)
        assert isinstance(v1, GraphVertex) and isinstance(v2, GraphVertex)
        self.v1, self.v2= v1, v2

    def connection( self, vertex_a ):
        if self.v1==vertex_a:
            return self.v2
        elif self.v2==vertex_a:
            return self.v1
        else:
            return None
    
    def __repr__(self):
        return "E"+"<"+str(self.v1)+","+str(self.v2)+">"



if __name__=="__main__":
    #example
    E= UndirectedGraphEdge
    V= GraphVertex
    print "creating loop with 4 vertices: a,b,c,d"
    a= V('a')
    b= V('b')
    c= V('c')
    d= V('d')
    E(a,b)
    E(b,c)
    E(c,d)
    E(d,a)
    print d,"is connected to:",d.adjacencyList()
