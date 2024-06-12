import matplotlib.pyplot as plt
from lib.MyDataSet import MyDataSet
class Graph:
    departure_obj = MyDataSet("International_Report_Departures.csv")
    passengers_obj = MyDataSet("International_Report_Passengers.csv")
    departure_df :any
    processData_df :any
    passengers_df :any
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
        self.departure_df = self.departure_obj.data_fram
        self.passengers_df = self.passengers_obj.data_fram
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
        elif(category == 2):
            if(choice == 1 ):
                self.draw_year(False,True)
            elif(choice == 2 ):
                self.draw_month(False,True)
        elif(category == 3):
            if(choice == 1 ):
                self.draw_year(True)
            elif(choice == 2 ):
                self.draw_month(True)
            elif(choice == 3 ):
                self.draw_date(True)
            elif(choice == 4 ):
                self.draw_year_month(True)
        elif(category == 4):
            if(choice == 1 ):
                self.draw_year(True,True)
            elif(choice == 2 ):
                self.draw_month(True,True)
        # elif(category == 5):
        #     if(choice == 1 ):
        #         self.draw_year(True,False,True)
        #     elif(choice == 2 ):
        #         self.draw_month(True,False,True)
        # elif(category == 6):
        #     if(choice == 1 ):
        #         self.draw_year(True,True,True)
        #     elif(choice == 2 ):
        #         self.draw_month(True,True,True)
        if((self.counter+1) >= self.count) :
            return False
        # else :
        return True
        
    def draw_month(self,passengers=False,and_carrier=False,airport=False) -> None :
        self.month_data(passengers,and_carrier,airport)
        self.draw_plot(self.processData["Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Total"],"Total")
        self.draw_plot(self.processData["Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Charter"],"Charter")
        self.draw_plot(self.processData["Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Scheduled"],"Scheduled")
        self.legend()
    def draw_year(self,passengers=False,and_carrier=False,airport=False) -> None :
        self.year_data(passengers,and_carrier,airport)
        self.draw_plot(self.processData["Year"] if not and_carrier else self.processData["Carrier Year"],self.processData["Total"],"Total")
        self.draw_plot(self.processData["Year"] if not and_carrier else self.processData["Carrier Year"],self.processData["Charter"],"Charter")
        self.draw_plot(self.processData["Year"] if not and_carrier else self.processData["Carrier Year"],self.processData["Scheduled"],"Scheduled")
        self.legend()
    def draw_year_month(self,passengers=False,and_carrier=False) -> None :
        self.year_month_data(passengers,and_carrier)
        self.draw_plot(self.processData["Year Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Total"],"Total")
        self.draw_plot(self.processData["Year Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Charter"],"Charter")
        self.draw_plot(self.processData["Year Month"] if not and_carrier else self.processData["Carrier Month"],self.processData["Scheduled"],"Scheduled")
        self.legend()
    def draw_date(self,passengers=False,and_carrier=False) -> None :
        self.date_data(passengers,and_carrier)
        self.draw_plot(self.processData["data_dte"],self.processData["Total"],"Total")
        self.draw_plot(self.processData["data_dte"],self.processData["Charter"],"Charter")
        self.draw_plot(self.processData["data_dte"],self.processData["Scheduled"],"Scheduled")
        self.legend()
    def year_data(self,passengers=False,and_carrier=False,airport=False):
        if(not passengers):
            if(and_carrier):
                self.departure_df["Carrier Year"] = self.departure_df.apply(lambda row: "{} - {}".format( str(row["carrier"]),str(row["Year"])), axis=1)
                self.processData  = self.departure_df.groupby(["Carrier Year"])[["Total","Charter","Scheduled"]].sum().reset_index()
            else:
                self.processData  = self.departure_obj.group_by_key_and_sum(keys=["Year"],sum_col=["Total","Charter","Scheduled"])
        else:
            if(and_carrier):
                self.passengers_df["Carrier Year"] = self.passengers_df.apply(lambda row: "{} - {}".format( str(row["carrier"]),str(row["Year"])), axis=1)
                self.processData  = self.passengers_df.groupby(["Carrier Year"])[["Total","Charter","Scheduled"]].sum().reset_index()
            else:
                self.processData  = self.passengers_obj.group_by_key_and_sum(keys=["Year"],sum_col=["Total","Charter","Scheduled"])
    def year_month_data(self,passengers=False):
        # self.departure_df["Year Month"] =  self.departure_df.apply(lambda row: "( {} - {} )".format(str(row["Year"]) , str(row["Month"])))
        if(not passengers):
            self.departure_df["Year Month"] = self.departure_df.apply(lambda row: "( {} - {} )".format(str(row["Year"]), str(row["Month"])), axis=1)
            self.processData  = self.departure_df.groupby(["Year Month"])[["Total","Charter","Scheduled"]].sum().reset_index()
        else:
            self.passengers_df["Year Month"] = self.passengers_df.apply(lambda row: "( {} - {} )".format(str(row["Year"]), str(row["Month"])), axis=1)
            self.processData  = self.passengers_df.groupby(["Year Month"])[["Total","Charter","Scheduled"]].sum().reset_index()
    def month_data(self,passengers=False,and_carrier=False,airport=False):
        if(not passengers):
            if(and_carrier):
                self.departure_df["Carrier Month"] = self.departure_df.apply(lambda row: "{} - {}".format( str(row["carrier"]),str(row["Month"])), axis=1)
                self.processData  = self.departure_df.groupby(["Carrier Month"])[["Total","Charter","Scheduled"]].sum().reset_index()
            else:
                self.processData  = self.departure_obj.group_by_key_and_sum(keys=["Month"],sum_col=["Total","Charter","Scheduled"])
        else:
            if(and_carrier):
                self.passengers_df["Carrier Month"] = self.passengers_df.apply(lambda row: "{} - {}".format( str(row["carrier"]),str(row["Month"])), axis=1)
                self.processData  = self.passengers_df.groupby(["Carrier Month"])[["Total","Charter","Scheduled"]].sum().reset_index()
            else:
                self.processData  = self.passengers_obj.group_by_key_and_sum(keys=["Month"],sum_col=["Total","Charter","Scheduled"])            
    def date_data(self,passengers=False):
        if(not passengers):
            self.processData  = self.departure_obj.group_by_key_and_sum(keys=["data_dte"],sum_col=["Total","Charter","Scheduled"])
        else:
            self.processData  = self.passengers_obj.group_by_key_and_sum(keys=["data_dte"],sum_col=["Total","Charter","Scheduled"])
    def draw_plot(self,x,y,t):
        if(self.y <= 1 and self.x <= 1):
            plt.plot(x,y,label=t)
        elif(self.x <= 1):
            self.axi[self.y_counter].plot(x,y,label=t)
        elif(self.y <= 1):
            self.axi[self.x_counter].plot(x,y,label=t)
        else:
            self.axi[self.x_counter,self.y_counter].plot(x,y,label=t)
    def legend(self):
        if(self.y <= 1 and self.x <= 1):
            plt.legend()
        elif(self.x <= 1):
            self.axi[self.y_counter].legend()
        elif(self.y <= 1):
            self.axi[self.x_counter].legend()
        else:
            self.axi[self.x_counter,self.y_counter].legend()
    def show(self) -> None :
        plt.show()
