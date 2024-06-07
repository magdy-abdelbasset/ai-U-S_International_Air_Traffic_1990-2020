import pandas as pd
import matplotlib.pyplot as plt
import os
class MyDataSet:
    data_fram = pd.DataFrame([])
    path_csv_file = ""
    dir_separator = os.sep
    def __init__(self,file):
        self.path_csv_file = "{}{}DataSet{}{}".format(os.getcwd(),self.dir_separator,self.dir_separator,file) 
        # print(self.path_csv_file)
        self.data_fram = pd.DataFrame(pd.read_csv(self.path_csv_file))
    def group_by_key_and_sum(self,keys=["Year"],sum_col=["Total"]):
        data_fram = self.data_fram
        return data_fram.groupby(keys)[sum_col].sum().reset_index()

