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
            inp.controls.append(ft.Text(value="+",weight="w700",size=30))
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
            inp.controls.append(ft.Text(value="-",weight="w700",size=30))
            m3=fletmat.fletwith(x.value,y.value)
            inp.controls.append(m3)
            page.update()        
    def ac(a):
        global count
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
        global mat2
        mat2=fletmat.fletwith(int(y.value),int(z.value))
        #fletmat.fletmat.printmat(mat1)
        inp.controls.append(mat2)
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
            inp.controls.append(ft.Text(value="x",weight="w700",size=30))
            enrow.controls=[
            ft.Text(value="How many columns: "),
            z:=ft.TextField(value="0",on_submit=c)]
            page.update()
    def trans(a):
        global operator
        global count
        operator="Tr"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{Transpose}",weight="w700",size=30))
            page.update()
    def trace(a):
        global count
        global operator
        operator="trace"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{Trace}",weight="w700",size=30))
            page.update()
    def square(a):
        global count
        global operator
        operator="sq"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{CheckSquare}",weight="w700",size=30))
            page.update()
    def deter(a):
        global count
        global operator
        operator="det"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{DET}",weight="w700",size=30))
            page.update()
    def inve(a):
        global count
        global operator
        operator="inv"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{INV}",weight="w700",size=30))
            page.update()
    def adj(a):
        global count
        global operator
        operator="adj"
        if count==1:
            count=2
            inp.controls.append(ft.Text(value="{ADJ}",weight="w700",size=30))
            page.update()    
    def end(e):
        val="{CoFactor}"+row.value+","+column.value
        inp.controls.append(ft.Text(value=val,weight="w700",size=30))
        enrow.controls.clear()
        page.update()
    
    def c2(a):
        global column
        enrow.controls=[column:=ft.TextField(
                label="Enter column",
                border_color="transparent",
                    keyboard_type="number",
                on_submit=end
                ),]
        page.update()
    def cof(a):
        global count
        global operator
        global row
        operator="cof"
        if count==1:
            count=2
            enrow.controls=[row:=ft.TextField(
                label="Enter row",
                border_color="transparent",
                    keyboard_type="number",
                on_submit=c2
                ),]
            page.update()
    def equal(a):
        #fletmat.fletmat.printmat(mat1)
        global mat3
        global operator
        if operator=='+':
            
            mat3=fletmat.fletmat.matadd(mat1,m2)
            inp.controls=[mat3]
            page.update()
        elif operator=='-':
            mat3=fletmat.fletmat.matsub(mat1,m3)
            inp.controls=[mat3]
            page.update()
        elif operator=="Tr":
            mat3=fletmat.fletmat.flet_transpose(mat1)
            inp.controls=[mat3]
            page.update()
        elif operator=="*":
            mat3=fletmat.fletmat.matmulti(mat1,mat2)
            inp.controls=[mat3]
            page.update()
        elif operator=="trace":
            res=fletmat.fletmat.flet_trace(mat1)
            inp.controls=[res]
            page.update()
        elif operator=="sq":
            res=fletmat.fletmat.flet_square(mat1)
            inp.controls=[res]
            page.update()
        elif operator=="det":
            res=fletmat.fletmat.flet_determinant(mat1)
            inp.controls=[res]
            page.update()
        elif operator=="inv":
            res=fletmat.fletmat.flet_inverse(mat1)
            inp.controls=[res]
            page.update()
        elif operator=="adj":
            res=fletmat.fletmat.flet_adjoint(mat1)
            inp.controls=[res]
            page.update()
        elif operator=="cof":
            res=fletmat.fletmat.flet_cofactor(mat1,int(row.value),int(column.value))
            inp.controls=[res]
            page.update()
        operator=''    
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
                ft.ElevatedButton(text="INV",expand=True,on_click=inve),
                ft.ElevatedButton(text="Tr",expand=True,on_click=trans),
                ft.ElevatedButton(text="Det",expand=True,on_click=deter),
            ],
     
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="isSq",expand=True,on_click=square),
                ft.ElevatedButton(text="trace",expand=True,on_click=trace),
                ft.ElevatedButton(text="Adj",expand=True,on_click=adj),
                ft.ElevatedButton(text="CoF",expand=True,on_click=cof),
            ],
        )
        ,ft.Row(
            controls=[    
                ft.ElevatedButton(text="x",expand=True,on_click=multi),
                ft.ElevatedButton(text="-",expand=True,on_click=minus),
                ft.ElevatedButton(text="+",expand=True,on_click=plus),
                ft.ElevatedButton(text="=",expand=True,on_click=equal),
                ],
            ),
        

        )
    
    
ft.app(target=main)
