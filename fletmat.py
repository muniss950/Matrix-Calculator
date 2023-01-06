import flet as ft
import matrix
'''def underline(st):
    return '{:s}'.format('\u0332'.join(st+' '))[:-1]'''  
       
class fletmat(ft.UserControl):
    def __init__(self,l=[[0,0,0],[0,0,0],[0,0,0]]):
        super().__init__()
        self.row=len(l[0])
        self.column=len(l)
        self.matrix=matrix.matrix(l)
        self.list=l
        self.a=self.lismat(l)
        #self.cursor=[0,0] #not needed now
        
    def lismat(self,l,x=0,y=0):          #to make a matrix when a list is given 
        items = []
        items.append(ft.Text(value="\n"))
       
        for i in range(len(self.list)):
            row=[]
            for j in range(len(self.list[i])):
                    row.append(
                    ft.Container(height=25,width=100,content=ft.TextField(value="0",text_align='center',border_color="Transparent",))
                )
            
            items.append(
            ft.Row(controls=row))
     
        return items
        
    def build(self,l=[[0,0,0],[0,0,0],[0,0,0]]):
        super().__init__()
        self.row=len(l[0])
        self.column=len(l)
        self.matrix=matrix.matrix(l)
        self.value=l
        #self.cursor=[0,0]
        self.a=self.lismat(l,)
        self.x=ft.Column(
                controls=
                self.a,
        
        )
        return ft.Row(
        controls=[
            ft.Text(value='[',size=40*(self.row),weight="w100"),
            self.x
            ,ft.Text(value=']',size=40*(self.row),weight="w100")],
    scroll=True,

    )

    '''def forward(self,):
        if self.cursor[1]==len(self.list[0])-1 and self.cursor[0]!=len(self.list)-1:
            self.cursor[0]+=1
            self.cursor[1]=0
        elif self.cursor[1]==len(self.list[0])-1 and self.cursor[0]==len(self.list)-1:
            pass
        else:
            self.cursor[1]+=1
        self.a=self.lismat(self.list,1,1)
        self.update()

    def backward(self,):
        if self.cursor[1]==len(self.list[0])-1 and self.cursor[0]!=0:
            self.cursor[0]-=1
            self.cursor[1]=len(self.list[0])-1
        elif self.cursor[1]==len(self.list[0])-1 and self.cursor[0]==len(self.list)-1:
            pass
        else:
            self.cursor[1]-=1'''

    def getmatrix(self,):
        return self.matrix

    def printmat(self,):
        print(self.matrix)

    def lenrow(self,):
        return len(self.list[0])

    def lencol(self,):
        return len(self.list)

    '''def changeval(self,x,y,inp):
        if self.cursor==[x,y]:
            self.a[x+1].controls[y].value=underline(str(inp))
        else:
            self.a[x+1].controls[y].value=str(inp)
        self.update()'''



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

    '''def getcursor(self,):
        return self.cursor'''
