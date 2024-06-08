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
    x = 0
    y = 0
    x_counter = -1
    y_counter = 0
    def __init__(self,x,y) -> None:
        self.fig ,self.axi = plt.subplots(x,y)
        self.count = x*y
        self.x = x
        self.y = y
    def draw(self,category,choice):
        if(self.x_counter >= self.x -1 ):
            self.y_counter += 1
            self.x_counter = -1
        self.x_counter += 1 
        self.counter = self.counter + 1
        if(category == 1):
            if(choice == 1 ):
                self.draw_year()
            elif(choice == 2 ):
                self.draw_month()
            elif(choice == 3 ):
                self.draw_date()
            elif(choice == 4 ):
                self.draw_year_month()
        if((self.counter+1) >= self.count) :
            return False
        # else :
        return True
        
    def draw_month(self) -> None :
        self.month_data()
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Total"],label="Total")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Charter"],label="Charter")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Scheduled"],label="Scheduled")
        self.axi[self.x_counter,self.y_counter].legend()
    def draw_year(self) -> None :
        self.year_data()
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Year"],self.year_flights["Total"],label="Total")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Year"],self.year_flights["Charter"],label="Charter")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Year"],self.year_flights["Scheduled"],label="Scheduled")
        self.axi[self.x_counter,self.y_counter].legend()
    def draw_year_month(self) -> None :
        self.year_month_data()
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Total"],label="Total")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Charter"],label="Charter")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["Month"],self.year_flights["Scheduled"],label="Scheduled")
        self.axi[self.x_counter,self.y_counter].legend()
    def draw_date(self) -> None :
        self.date_data()
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["data_dte"],self.year_flights["Total"],label="Total")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["data_dte"],self.year_flights["Charter"],label="Charter")
        self.axi[self.x_counter,self.y_counter].plot(self.year_flights["data_dte"],self.year_flights["Scheduled"],label="Scheduled")
        self.axi[self.x_counter,self.y_counter].legend()
    def year_data(self):
        self.year_flights  = self.departure_obj.group_by_key_and_sum(keys=["Year"],sum_col=["Total","Charter","Scheduled"])
    def year_month_data(self):
        self.year_flights  = self.departure_obj.group_by_key_and_sum(keys=["Year","Month"],sum_col=["Total","Charter","Scheduled"])
    def month_data(self):
        self.year_flights  = self.departure_obj.group_by_key_and_sum(keys=["Month"],sum_col=["Total","Charter","Scheduled"])
    def date_data(self):
        self.year_flights  = self.departure_obj.group_by_key_and_sum(keys=["data_dte"],sum_col=["Total","Charter","Scheduled"])
    def show(self) -> None :
        plt.show()