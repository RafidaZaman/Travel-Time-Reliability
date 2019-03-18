import xlrd


loc = ('C:/Users/Mihran/Desktop/PYTicas results/Incidents only data/I-35W (NB) - 03 Minneapolis Downtown to I694 All files/2013 traveltime-data.xlsx')

series = xlrd.open_workbook(loc)
sheet = series.sheet_by_index(1)
print(sheet.row([0]))
# For row 0 and column 0
sheet.cell_value(3, 4)
print(sheet.cell_value(3,1))
# Extracting number of columns
print(sheet.nrows)


