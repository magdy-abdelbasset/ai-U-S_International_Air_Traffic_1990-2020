class BashUi :
    page = 1
    rows = 2
    columns = 2
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
    def first_page(self) -> None :
        print("What You Want")
        print("1. رسومات تحليل بالتاريخ/Analysis Drawings By History")
        return input("Enter Your Choice And Click Enter :-")
        # print("|                 - Welcom In U.S International Air Traffic 1990-2020 -                 |")
        # print("----------------------------------------------------------------------------------------")