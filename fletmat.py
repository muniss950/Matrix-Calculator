import flet as ft

def yinput(c):
        y=[]
        for i in range(1,c+1):
            y.append(
                ft.Text(value='0')
            )
        return y
def xinput(r,c):
        items = []
        items.append(ft.Text(value="\n"))
        for i in range(1, r + 1):
            items.append(
            ft.Row(controls=yinput(c)))
            
        return items


class fletmat(ft.UserControl):
    def __init__(self,row,column):
        super().__init__()
        self.row=row
        self.column=column
    def build(self,):
        return ft.Row(
        controls=[
            ft.Text(value='[',size=40*(self.row),weight="w100"),
            ft.Column(
                controls=
                xinput(self.row,self.column),
        
        ),ft.Text(value=']',size=40*(self.row),weight="w100")],
    scroll=True,

    )


