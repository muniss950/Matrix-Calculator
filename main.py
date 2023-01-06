import flet as ft
import fletmat

    
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
    page.window_width=500
    page.window_left=500
    page.window_top=200
    page.window_resizable=False
    page.scroll=True
    #b=fletmat.fletmat([[1,1],[0,0]])
    #c=fletmat.fletmat([[2,2],[1,1]])
    result=fletmat.fletmat()
    x=ft.Row(controls=[result])
    #print(fletmat.fletmat.getcursor(result))
    '''def x(a):
        s=ft.Row(controls=[ft.Text(value="m")]) 
        page.add(s)
        page.update()'''
    
    
     
   
    #fletmat.fletmat.printmat(result) #//to print on terminal
    #print(fletmat.fletmat.lenrow(result))
    def plus(a):
        x.controls.append(ft.Text(value="+"))
        m2=fletmat.fletmat()
        x.controls.append(m2)
        page.update()
    page.add(
        
        x,
        ft.Row(controls=[
                
                enter:=ft.TextField(
                label="Enter here",
                border_color="transparent",
                    keyboard_type="number",
                #on_submit=click
                ),
                
                ],),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC",expand=True),
                ft.ElevatedButton(text="INV",expand=True),
                ft.ElevatedButton(text="Tr",expand=True),
                ft.ElevatedButton(text="Sp.O",expand=True),
            ],
     
        ),
        ft.Row(
            controls=[    
                ft.ElevatedButton(text="x",expand=True),
                ft.ElevatedButton(text="-",expand=True),
                ft.ElevatedButton(text="+",expand=True,on_click=plus),
                ft.ElevatedButton(text="=",expand=True,),
                ],
            ),
        

        )
    
    
ft.app(target=main)
