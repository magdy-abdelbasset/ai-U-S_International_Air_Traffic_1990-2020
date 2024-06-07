from lib.BashUi import BashUi
from lib.Graph import Graph
def __init__():
    ui = BashUi()
    graph = Graph()
    input = ui.start()
    input = int(input) if input.isnumeric() else 0 
    num = input * ui.page
    while(input != 0 ):
        print("num >>> %d"%num)
        graph.draw(num=num)
        if(ui.page == 1):
            input = ui.first_page()
            input = int(input) if input.isnumeric() else 0 
            num = input * ui.page
    graph.show()
__init__()
