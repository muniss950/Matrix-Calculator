from copy import deepcopy
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
    def is_square(self):
        if len(self.a)==len(self.a[0]):
            return True
        else:
            return False
    def transpose(self):
        res=matrix([[0 for j in range(len(self.a))] for i in range(len(self.a[0]))])
        #print(res)
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                #print(i,j)
                res.a[j][i]=self.a[i][j]
        return res         
    
    def __add__(self,rmat):      #special function for defining addition
        c=rmat.mat_getlist()
        b=self.mat_getlist()
        res= [[0 for j in range(len(c[i]))] for i in range(len(c))]
        for i in range(len(b)):
            for j in range(len(b[i])) :
                res[i][j]=c[i][j]+b[i][j]
        t=matrix(res)
        return t
    def __sub__(self,rmat):      #special function for defining addition
        c=rmat.mat_getlist()
        b=self.mat_getlist()
        for i in range(len(b)):
            for j in range(len(b[i])) :
                b[i][j]-=c[i][j]
        t=matrix(b)
        return t

    def __mul__(self,rmat):
        c=rmat.mat_getlist()
        b=self.mat_getlist()
        if len(c[0])==len(b):
            res=([[0 for j in range(len(b)) ]for i in range(len(c[0]))])
            #print(res)
            d=rmat.transpose().mat_getlist()
            for row_self in range(len(b)):
                for row_transpose in range(len(d)):
                    new_element=0
                    for column_self in range(len(b[0])):
                        new_element+=(b[row_self][column_self]*d[row_transpose][column_self])
                    #print(row_self,row_transpose)
                    res[row_self][row_transpose]=new_element
            return matrix(res)
        else:
            raise ValueError("no of columns in first matrix must be equal to no of rows in second matrix")    
    def scalar_product(self, number):
        newMatrix =[[0 for j in range(len(self.a[0]))] for i in range(len(self.a))]

        for row in range(len(self.a)):
            for column in range(len(self.a[0])):
                newMatrix[row][column] = self.a[row][column] * number

        return matrix(newMatrix)
    
    
    def trace(self):
        if self.is_square():
            res=0
            for i in range(len(self.a)):
                res+=self.a[i][i]
            return res
        else:
            raise ValueError("Matrix needs to be square.")
    def complement_matrix(self, rowToDelete, columnToDelete):
        newMatrix = deepcopy(self).mat_getlist()
        del(newMatrix[rowToDelete])

        for row in range(len(newMatrix)):
            del(newMatrix[row][columnToDelete])

        #newMatrix.columns -= 1

        return matrix(newMatrix)
    
    def algebric_complement(self, row, column):
        complementMatrix = self.complement_matrix(row, column)
        algebricComplement = (-1)**(row+column) * complementMatrix.determinant()

        return (algebricComplement)

    def determinant(self):
        '''
        Return the determinant.
        This function uses Laplace's theorem to calculate the determinant.
        It is a very rough implementation, which means it becomes slower and
        slower as the size of the matrix grows.
        '''
        b=self.mat_getlist()
        if self.is_square():
            if len(b) == 1:
                # If it's a square matrix with only 1 row, it has only 1 element
                det = b[0][0] # The determinant is equal to the element
            elif len(b) == 2:
                det = (b[0][0] * b[1][1]) - (b[0][1] * b[1][0])
            else:
                # We calculate the determinant using Laplace's theorem
                det = 0
                for element in range(len(b[0])):
                    det += b[0][element] * (self.algebric_complement(0, element))
            return det
        else:
            raise TypeError("Can only calculate the determinant of a square matrix")

    def algebric_complements_matrix(self):
        '''Return the matrix of all algebric complements.'''
        if self.is_square():
            newMatrix = [[0 for j in range(len(self.a[0]))] for i in range(len(self.a))]
            for row in range(len(self.a)):
                for column in range(len(self.a[0])):
                    newMatrix[row][column] = self.algebric_complement(row, column)
            return matrix(newMatrix)
        else:
            raise TypeError("Algebric complements can only be calculated on a square matrix")
    def adjoint(self):
        return self.algebric_complements_matrix().transpose()
    def inverse_matrix(self):
        '''Return the inverse matrix.'''
        det = self.determinant()
        if det == 0:
            raise Exception("Matrix not invertible")
        else:
            algebricComplementsMatrix = self.algebric_complements_matrix()
            inverseMatrix =  algebricComplementsMatrix.transpose().scalar_product(1/det)

            return inverseMatrix

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
