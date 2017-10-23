import pandas as pd
import numpy as np
import sys


def convertExcelToCsv(file):
    data = pd.read_excel(file, sheetname = "Indeksit")
    data['Date & Time'] = data['Date & Time'].str.replace('24:00', '23:59')
    data.replace(["NoData", "OffScan"], np.NaN, inplace=True)
    
    data["Date & Time"] = pd.to_datetime(data["Date & Time"])
    data = data.set_index(data["Date & Time"])
    
    year = str(data["Date & Time"][1].year)
    data = data.drop(['Date & Time'],1)
    
    data.to_csv("./resources/raw_data" + year +".csv")

args = sys.argv
if(len(args) == 2):
    convertExcelToCsv(args[1])
else:
    for i in range(2014,2018):
        file = './resources/excel-files/Ilmanlaatuindeksit' + str(i) + '.xlsx'
        convertExcelToCsv(file)
