import flet as ft
import matrix

def lismat(l):          #to make a matrix when a list is given 
    items = []
    items.append(ft.Text(value="\n"))
    for i in range(len(l)):
            row=[]
            for j in l[i]:
                row.append(
                    ft.Text(value=str(j))
                )
            
            items.append(
            ft.Row(controls=row))
     
    return items

class fletmat(ft.UserControl):
    def __init__(self,l=[[0,0,0],[0,0,0],[0,0,0]]):
        super().__init__()
        self.row=len(l[0])
        self.column=len(l)
        self.matrix=matrix.matrix(l)
        self.list=l
    def build(self,):
        return ft.Row(
        controls=[
            ft.Text(value='[',size=40*(self.row),weight="w100"),
            ft.Column(
                controls=
                lismat(self.list),
        
        ),ft.Text(value=']',size=40*(self.row),weight="w100")],
    scroll=True,

    )
    def getmatrix(self,):
        return self.matrix
    def printmat(self,):
        print(self.matrix)
    def lenrow(self,):
        return len(self.list[0])
    def lencol(self,):
        return len(self.list)
    def changeval(self,x,y,inp):
        a=self.getmatrix()
        
        self.list[x][y]=inp
        
        self.update()
        super().update()
        return fletmat(self.list)
    def matadd(self,rmat):
        a=self.getmatrix()
        b=rmat.getmatrix()
        c=a+b
        d=matrix.matrix.mat_getlist(c)
        return fletmat(d)
    def matsub(self,rmat):
        a=self.getmatrix()
        b=rmat.getmatrix()
        c=a-b
        d=matrix.matrix.mat_getlist(c)
        return fletmat(d)
