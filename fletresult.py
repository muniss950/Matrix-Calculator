import flet as ft
#import matrix

class fletresult(ft.UserControl):
    def __init__(self,l):
        super().__init__()
        #l=[[0 for i in range(x)] for j in range(y)]
        self.row=len(l[0])
        self.column=len(l)
        
        self.list=l
        #self.a=self.lismat(l)
        #self.matrix=matrix.matrix(l)
        #self.matrix=matrix.matrix(self.lismat(l)[1])
        #self.cursor=[0,0] #not needed now
    
    def lismat(self,l):          #to make a matrix when a list is given 
        
        
        items = []
        
        items.append(ft.Text(value="\n"))
        #val=[[0 for j in range(len(l[i])-1)] for i in range(len(l)-1)]
        for i in range(len(l)):
            row=[]  
            for j in l[i]:
                    f=ft.TextField(value=str(j),text_align='center',border_color="Transparent")
                    #f=ft.TextField(value="0",text_align='center',border_color="Transparent",on_change=change)
                    row.append(
                    ft.Container(height=25,width=100,content=(f))# '''on_change=fletmat.changeval'''))
                    )
                    '''row.append(
                    f)'''# '''on_change=fletmat.changeval'''))
                    
                    
            items.append(
            ft.Row(controls=row))
        #print(tf[f])
        return items
    def build(self,):
        super().__init__()
        #self.row=len(l[0])
        #self.column=len(l)
        #self.list=l
        #self.matrix=matrix.matrix(self.list)
        
        #self.value=l
        #self.cursor=[0,0]
        #self.a=self.lismat(l)
        self.x=ft.Column(
                controls=
                self.lismat(self.list),
        
        )
        return ft.Row(
        controls=[
            ft.Text(value='[',size=40*(self.row),weight="w100"),
            self.x
            ,ft.Text(value=']',size=40*(self.row),weight="w100")],
    scroll=True,

    )