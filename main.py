import flet as ft
import fletmat
import fletresult
    
def main(page: ft.Page):

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CALCULATE),
        leading_width=40,
        title=ft.Text("Matrix Calculator"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        )
    page.title="Matrix"
    page.window_height=500
    page.window_width=1000
    page.window_left=500
    page.window_top=200
    page.window_resizable=False
    page.scroll=True
    #b=fletmat.fletmat([[1,1],[0,0]])
    #c=fletmat.fletmat([[2,2],[1,1]])
    #result=fletmat.fletmat()
    #x=ft.Row(controls=[result])
    #print(fletmat.fletmat.getcursor(result))
    
    '''def x(a):
        s=ft.Row(controls=[ft.Text(value="m")]) 
        page.add(s)
        page.update()'''
    #mat=fletmat.fletmat()
    global count
    count=0          # to limit operation to only one
    global operator 
    operator=''
    def b(a):
        #mat=fletmat.fletmat()
        global count
        global mat1
        count=1
        #print(x.value,y.value)
        mat1=fletmat.fletwith(int(x.value),int(y.value))
        #fletmat.fletmat.printmat(mat1)
        inp.controls=[mat1]
        
        page.update()
    y=ft.TextField(value="0",on_submit=b)
    
    
    def at(a):
        inp.controls.clear()
        inp.controls.append(ft.Text(value="How many column"))
        inp.controls.append(y)
        page.update()
    x=ft.TextField(value="0",on_submit=at)
    inp=ft.Row(controls=[
        ft.Text(value="How many rows: "),
        x]) 
   
    #fletmat.fletmat.printmat(result) #//to print on terminal
    #print(fletmat.fletmat.lenrow(result))
    def plus(a):
        global count
        global operator
        operator='+'
        global m2
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="+"))
            m2=fletmat.fletwith(x.value,y.value)
            inp.controls.append(m2)
            page.update()
    def minus(a):
        global count
        global operator 
        operator='-'
        global m3
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="-"))
            m3=fletmat.fletwith(x.value,y.value)
            inp.controls.append(m3)
            page.update()        
    def ac(a):
        global count
        #global x
        count=0
        inp.controls=[
        ft.Text(value="How many rows: "),
        x]
        page.update()
    def c(a):
        count=2
        #print(x.value,y.value)
        global z
        global mat1
        mat1=fletmat.fletwith(int(y.value),int(z.value))
        #fletmat.fletmat.printmat(mat1)
        inp.controls.append(mat1)
        enrow.controls=[enter:=ft.TextField(
                label="Enter here",
                border_color="transparent",
                    keyboard_type="number",
                #on_submit=click
                ),]
        page.update()
    def multi(a):
        global z
        global count
        global operator 
        operator='*'
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="x"))
            enrow.controls=[
            ft.Text(value="How many columns: "),
            z:=ft.TextField(value="0",on_submit=c)]
            page.update()
    def equal(a):
        #fletmat.fletmat.printmat(mat1)
        if operator=='+':
            
            mat3=fletmat.fletmat.matadd(mat1,m2)
            inp.controls=[mat3]
            page.update()
        elif operator=='-':
            mat3=fletmat.fletmat.matsub(mat1,m3)
            inp.controls=[mat3]
            page.update()    
    page.add(
        inp,
        #x,
        #mat,
        enrow:=ft.Row(controls=[
                
                enter:=ft.TextField(
                border_color="transparent",
                    keyboard_type="number",
                #on_submit=click
                ),
                
                ],),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC",expand=True,on_click=ac),
                ft.ElevatedButton(text="INV",expand=True),
                ft.ElevatedButton(text="Tr",expand=True),
                ft.ElevatedButton(text="Det",expand=True),
            ],
     
        ),
        ft.Row(
            controls=[    
                ft.ElevatedButton(text="x",expand=True,on_click=multi),
                ft.ElevatedButton(text="-",expand=True,on_click=minus),
                ft.ElevatedButton(text="+",expand=True,on_click=plus),
                ft.ElevatedButton(text="=",expand=True,on_click=equal),
                ],
            ),
        

        )
    
    
ft.app(target=main))
