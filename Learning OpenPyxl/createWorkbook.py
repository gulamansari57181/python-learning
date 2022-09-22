# Openpyxl only deals with the .xlsx workbook

# import openpyxl
import openpyxl

# initialzing a workbook
wb = openpyxl.Workbook()

# save the workbook with a name
# wb.save("MyWorkbook.xlsx")

# open an existing .xlsx file
wb = openpyxl.load_workbook("MyWorkbook.xlsx")

# traversing each sheet
for sheet in wb:
    print(sheet.title)

