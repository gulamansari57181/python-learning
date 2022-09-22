from openpyxl import load_workbook

wb = load_workbook("CRUD on Workbook.xlsx")

for sheet in wb:
    print(sheet.title)

source_sheet = wb["First Sheet"]

new_sheet = wb.copy_worksheet(source_sheet)

# giving title to copied sheet

new_sheet.title = "New Copied Sheet"

for sheet in wb:
    print(sheet.title)
    
wb.save("CopiedSheet.xlsx")

# getting sheet by name and index
for sheet in wb:
    print(f"Sheet name is  {sheet.title} at an index {wb.index(sheet)}")