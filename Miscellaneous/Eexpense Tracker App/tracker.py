# Project : Add your expenses with system generated fate into a csv file using csv module and file handeling methods in python.


import csv
from datetime import date

# Todays date
# print(date.today())
dt = date.today()

# converting date into specfic string format
dt = dt.strftime("%d/%m/%y")
print(dt)
# output: 21/09/22

# Creating a csv file
filename = "text.csv"

expenses = []
isStopped = False

# open file in write mode 
with open(filename,"a",newline="") as file:
    csvwriter = csv.writer(file)
    # writing today's date in a row will cause error because it expect an iteratabale where as return type of date is not same 
    # csvwriter.writerow(dt)
    while not isStopped:
     xp = int(input("Write your expenses(type 0 to stopped)"))
     if xp !=0:
            csvwriter.writerow([dt,xp])
            # output to csv file : 21/09/22
            expenses.append(xp)
     else:
        isStopped = True
print(expenses) 
print(f"Total expenses for today is {sum(expenses)}")    
file.close()    
