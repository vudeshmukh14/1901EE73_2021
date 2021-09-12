import csv
import os
from openpyxl import Workbook,load_workbook

def output_by_subject(new_row, heading):
    if os.path.isdir("output_by_subject")==False:
        os.mkdir("output_by_subject")
    path=r"output_by_subject\\"
    if os.path.exists(path+'%s.xlsx' %new_row[2]) == False:
        wb = Workbook()
        sheet = wb.active
        sheet.append(heading)
        wb.save(path+'%s.xlsx' %new_row[2])

    wb = load_workbook(path+'%s.xlsx' %new_row[2])
    sheet = wb.active
    sheet.append(new_row)
    wb.save(path+'%s.xlsx' %new_row[2])
    return

def output_individual_roll(new_row, heading):
    if os.path.isdir("output_individual_roll")==False:
        os.mkdir("output_individual_roll")
    path=r"output_individual_roll\\"
    if os.path.exists(path+'%s.xlsx' %new_row[0]) == False:
        wb = Workbook()
        sheet = wb.active
        sheet.append(heading)
        wb.save(path+'%s.xlsx' %new_row[0])

    wb = load_workbook(path+'%s.xlsx' %new_row[0])
    sheet = wb.active
    sheet.append(new_row)
    wb.save(path+'%s.xlsx' %new_row[0])
    return


with open('regtable_old.csv', 'r') as file:      
    reader = csv.reader(file)
    cnt = 0
    heading=[]
    for row in reader:
        if  cnt == 0:
            heading=[row[0],row[1],row[3],row[8]]
            cnt += 1
        else:
            new_row=[row[0],row[1],row[3],row[8]] 
            output_individual_roll(new_row, heading)
            output_by_subject(new_row, heading)