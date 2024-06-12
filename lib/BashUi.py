class BashUi :
    page = 1
    rows = 2
    columns = 2
    num_categories = 6
    def __init__(self) -> None:
        pass
    def start(self) -> None :
        page = 1
        self.print_welcom()
    def print_enter_row(self):
        print("i'm here to help you")
        return input("Please Enter Count Rows You Need   : -  ")
    def print_enter_column(self,rows):
        print("count rows know is %d"%rows)
        return input("Please Enter Count Column You Need   : -  ")
    def print_welcom(self) -> None :
        print("                                                                                        ")
        print("                                                                                        ")
        print("----------------------------------------------------------------------------------------")
        print("|                              - You Are Welcom -                                       |")
        print("|                 - Welcom In U.S International Air Traffic 1990-2020 -                 |")
        print("----------------------------------------------------------------------------------------")
        print("                                                                                        ")
        print("                                                                                        ")
    def categories_page(self) -> None :
        print("What You Want")
        print("1 -  Analysis Count Flights By History")
        print("2 -  Analysis Count Flights By History And Carrier")
        print("3 -  Analysis Count Passengers By History")
        print("4 -  Analysis Count Passengers By History And Carrier")
        # print("5 -  Analysis Count Passengers By History And Airport")
        # print("6 -  Analysis Count Passengers By History , Airport And Carrier")
        self.print_exit()
        return input("Enter Your Choice And Click Enter    :-   ")
    def pageByCategory(self,category):
        if(category == 1):        
            print("What You Want")
            print("1 -  Analysis Count Flights By Years")
            print("2 -  Analysis Count Flights By Months")
            print("3 -  Analysis Count Flights By Date")
            print("4 -  Analysis Count Flights By Years And Months")
        elif(category == 2):
            print("What You Want")
            print("1 -  Analysis Count Flights By Years And Carrier")
            print("2 -  Analysis Count Flights By Months And Carrier")
        elif(category == 3):
            print("What You Want")
            print("1 -  Analysis Count Passengers By Years")
            print("2 -  Analysis Count Passengers By Months")
            print("3 -  Analysis Count Passengers By Date")
            print("4 -  Analysis Count Passengers By Years And Months")
        elif(category == 4):
            print("What You Want")
            print("1 -  Analysis Count Passengers By Years And Carrier")
            print("2 -  Analysis Count Passengers By Months And Carrier")
        # elif(category == 5):
        #     print("What You Want")
        #     print("1 -  Analysis Count Flights By Years And Carrier")
        #     print("2 -  Analysis Count Flights By Months And Carrier")
        # elif(category == 6):
        #     print("What You Want")
        #     print("1 -  Analysis Count Flights By Years And Carrier")
        #     print("2 -  Analysis Count Flights By Months And Carrier")
        self.print_back()
        self.print_exit()
        return input("Enter Your Choice And Click Enter    :-   ")
    def print_exit(self):
        print(". - if you want exit press any char not numeric and press Enter")
    def print_back(self):
        print("0 - For Prev Page")
        # print("|                 - Welcom In U.S International Air Traffic 1990-2020 -                 |")
        # print("----------------------------------------------------------------------------------------")