import matplotlib.pyplot as plt
from lib.MyDataSet import MyDataSet
def __init__():
    departure_obj = MyDataSet("International_Report_Departures.csv")
    year_flights = departure_obj.group_by_key_and_sum(keys=["Year"],sum_col=["Total","Charter","Scheduled"])
    plt.plot(year_flights["Year"],year_flights["Total"],label="Total")
    plt.plot(year_flights["Year"],year_flights["Charter"],label="Charter")
    plt.plot(year_flights["Year"],year_flights["Scheduled"],label="Scheduled")
    plt.legend()
    plt.show()
__init__()
