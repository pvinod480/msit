import openpyxl
import re
wb = openpyxl.Workbook()
sheet = wb["Sheet"]
wb.remove(sheet)
filenames = ["Elections2004.txt","Elections2009.txt","Elections2014.txt"]
pat = '[^0-9]'
for filename in filenames:
    fobj = open(filename,"r")
    year = re.sub(pat,"",filename)
    sheet = wb.create_sheet(year)

    for row,line in enumerate(fobj):
        fields = line.split()
        fields[5] = int(fields[5])
        fields[9] = int(fields[9])
        sheet.append(fields)
wb.save("Election data set.xlsx")
