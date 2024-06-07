import matplotlib.pyplot as plt
from lib.MyDataSet import MyDataSet
class Graph:
    departure_obj = MyDataSet("International_Report_Departures.csv")
    year_flights = MyDataSet("International_Report_Passengers.csv")
    passengers_obj :any
    fig :any
    axi :any
    count =-1
    counter = -1
    def __init__(self,y=3) -> None:
        self.fig ,self.axi = plt.subplots(3,3)
        self.count = y
        pass
    def draw(self,num):
        self.counter += 1
        if(num == 1):
            self.draw_year()
    def draw_year(self) -> None :
        self.year_data()
        self.axi[0,self.counter].plot(self.year_flights["Year"],self.year_flights["Total"],label="Total")
        self.axi[0,self.counter].plot(self.year_flights["Year"],self.year_flights["Charter"],label="Charter")
        self.axi[0,self.counter].plot(self.year_flights["Year"],self.year_flights["Scheduled"],label="Scheduled")
        self.axi[0,self.counter].legend()
    def year_data(self):
        self.year_flights  = self.departure_obj.group_by_key_and_sum(keys=["Year"],sum_col=["Total","Charter","Scheduled"])
    def show(self) -> None :
        plt.show()