import flet as ft
import matrix
'''def underline(st):
    return '{:s}'.format('\u0332'.join(st+' '))[:-1]'''  
      
class fletmat(ft.UserControl):
    def __init__(self,l=[[0,0,0],[0,0,0],[0,0,0]]):
        super().__init__()
        #l=[[0 for i in range(x)] for j in range(y)]
        self.row=len(l[0])
        self.column=len(l)
        
        self.list=self.lismat(l)[1]
        self.a=self.lismat(l)[0]
        #self.matrix=matrix.matrix(l)
        self.matrix=matrix.matrix(self.lismat(l)[1])
        #self.cursor=[0,0] #not needed now

    '''def __init__(self,x=3,y=3):
        super().__init__()
        l=[[0 for i in range(x)] for j in range(y)]
        self.row=len(l[0])
        self.column=len(l)
        self.matrix=matrix.matrix(l)
        self.list=l
        self.a=self.lismat(l)'''        
    def lismat(self,l,x=0,y=0):          #to make a matrix when a list is given 
        #global t
        def change(e):
                        self.list[tf[e.control][0]][tf[e.control][1]]=int(e.control.value)
                        #print(i,j) 
                        self.update()
        
        items = []
        tf={}
        items.append(ft.Text(value="\n"))
        val=[[0 for j in range(len(l[i])-1)] for i in range(len(l)-1)]
        for i in range(len(l)):
            row=[]  
            for j in range(len(l[i])):
                    
                    f=ft.TextField(value="0",text_align='center',border_color="Transparent",on_change=change)
                    row.append(
                    ft.Container(height=25,width=100,content=(f))# '''on_change=fletmat.changeval'''))
                    )
                    '''if j!=len([i])-1:
                        tf.append(f)'''
                    
                    tf[f]=[i,j]
                        
                
            
            items.append(
            ft.Row(controls=row))
        #print(tf[f])
        return items,val,tf
        
    def build(self,l=[[0,0,0],[0,0,0],[0,0,0]]):
        super().__init__()
        #self.row=len(l[0])
        #self.column=len(l)
        self.list=self.lismat(l)[1]
        self.matrix=matrix.matrix(self.list)
        
        #self.value=l
        #self.cursor=[0,0]
        #self.a=self.lismat(l,)
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

    def changeval(self,x,y,inp):
        self.a[x+1].controls[y].value=str(inp)
        self.update()



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
def fletwith(x,y): #creating matrix with no of columns
    lst=[[5 for i in range(int(y))] for j in range(int(x))]
    m=fletmat(lst)
    m.matrix=matrix.matrix(lst)
    return m    
        
'''def getcursor(self,):
        return self.cursor'''
