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
    input = 1
        # num = input * ui.page
    num = 1
    while(input != 0 and draw ):
        # input = ui.first_page()
        # input = int(input) if input.isnumeric() else 0 
        if(ui.page == 1):
            input = ui.first_page()
            input = int(input) if input.isnumeric() else 0 
            num = input * ui.page
        draw = graph.draw(num=num)
    graph.show()
__init__()
