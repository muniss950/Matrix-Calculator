class matrix(object):
    
    def __init__(self,a): #defining matrix
            for i in range(len(a)):
                if len(a[i])!=len(a[0]):
                    raise ValueError("Number of elements not uniform")
            self.a=list(a)
            self.__reduce__()
    
    def setvalue(self,b,x,y):   # b: value,x=row position,y:column postition
        self.a[x][y]=b
    
    def mat_getlist(self):    #get the list form for matrix
        return self.a
    def lenrow(self,):
        return len(self.a[0])
    def lencolumn(self,):
        return len(self.a)
    def add_row(self,e,x):    # to add a new row in matrix
        if len(e)!=len(self.a[0]):
            raise ValueError("Number of elements not uniform")
        self.a.insert(x,e)
    
    def add_column(self,e,y):      #to add new column
        if len(self.a)!=len(e):
            raise ValueError("Number of elements not unifrom")
        for i in range(len(self.a)):
            self.a[i].insert(y,e[i]) 
    def checksquare(self):
        if len(self.a)==len(self.a[0]):
            return True
        else:
            return False
    
    
    def __add__(self,rmat):      #special function for defining addition
        c=rmat.mat_getlist()
        b=self.mat_getlist()
        for i in range(len(b)):
            for j in range(len([i])) :
                b[i][j]+=c[i][j]
        t=matrix(b)
        return t
    def __sub__(self,rmat):      #special function for defining addition
        c=rmat.mat_getlist()
        b=self.mat_getlist()
        for i in range(len(b)):
            for j in range(len([i])) :
                b[i][j]-=c[i][j]
        t=matrix(b)
        return t

    
    
    def __str__(self):   #for printing matrix

        def s(q):
            x=''
            for i in q:
                for j in i:
                    x+=str(j)
                    x+='  '
                x+="\n"
            return x

        return s(self.a)    
