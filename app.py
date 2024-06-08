from lib.BashUi import BashUi
from lib.Graph import Graph
import math
def __init__():
    rows = ""
    columns = ""
    ui = BashUi()
    ui.start()
    while(rows == ""):
        rows = ui.print_enter_row()
        rows = int(rows) if rows.isnumeric() else ""
    while(columns == ""):
        columns = ui.print_enter_column(rows)
        columns = int(columns) if columns.isnumeric() else ""
    graph = Graph(rows,columns)
    draw = True
    category = 1
    choice = -1
    while(category != 0 and draw ):
        # if(ui.page == 1):
        category = ui.categories_page()
        category = int(category) if category.isnumeric() else 0 
        if(category > 0 and category <= ui.num_categories ):
            ui.page = 2
            choice = ui.pageByCategory(category)
            choice = int(choice) if choice.isnumeric() else -1               
            if(choice == -1):
                category = 1
            elif(choice == 0 ):  
                ui.page == 1
                continue
        draw = graph.draw(category ,choice)
    graph.show()
__init__()
