import pandas as pd
from matplotlib import pyplot
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
#loc = ('C:/Users/Mihran/Desktop/PYTicas results/Incidents only data/I-35W (NB) - 03 Minneapolis Downtown to I694 All files/2013 traveltime-data.xlsx')
pd.options.display.max_rows = 999
#series = xlrd.open_workbook(loc)
series = pd.read_excel('C:/Users/Mihran/Desktop/PYTicas results/Incidents only data/I-35W (NB) - 03 Minneapolis Downtown to I694 All files/2013 traveltime-data.xlsx', sheetname='data (OC=0)')

OperatingCondition = series['Operating Condition:']
OnlyIncident = series['OnlyIncident']
print(series['OnlyIncident'])
pyplot(series['OnlyIncident'])