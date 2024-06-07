class BashUi :
    page = 1
    def __init__(self) -> None:
        pass
    def start(self) -> None :
        page = 1
        self.print_welcom()
        return self.first_page()
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