import os
import csv

inputFilePath = os.path.join('Resources','budget_data.csv')

# define variables
TotalMonths = []
TotalAmount = []
MonthlyChangeProfit = []

MonthlyChange = 0
MonthlyChangeTotal = 0
InitialProfitCounter = 0

# open file to use
with open(inputFilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

# for loop
    for row in csvreader:
        TotalMonths.append(row[0])
        SumMonths = len(TotalMonths)
        TotalAmount.append(float(row[1]))
        ProfitForMonth = int(row[1])
        MonthlyChange = float(ProfitForMonth)
        MonthlyChangeTotal = MonthlyChangeTotal + MonthlyChange
        InitialProfitCounter = int(row[1])
        MonthlyChangeProfit.append(MonthlyChange)
        MaxProfit = max(MonthlyChangeProfit)
        MaxIndex = MonthlyChangeProfit.index(MaxProfit)
        MinProfit = min(MonthlyChangeProfit)
        MinIndex = MonthlyChangeProfit.index(MinProfit)
        AvgChangeProfit = round(MonthlyChangeTotal/SumMonths)
        SumAmount = sum(TotalAmount)

# print to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {SumMonths}')
print(f'Total Amount: ${SumAmount}')
print(f'Average Monthly Change: ${AvgChangeProfit}')
print(f'Greatest Increase in Profits: {TotalMonths[MaxIndex]} ${MaxProfit}')
print(f'Greatest Decrease in Profits: {TotalMonths[MinIndex]} ${MinProfit}')

# output to file
output = open('Analysis/result.txt', 'w')
output.write(f'''
Financial Analysis
------------------
Total Months: {SumMonths}
Total: ${SumAmount}
Average Monthly Change: ${AvgChangeProfit}
Greatest Increase in Profits: {TotalMonths[MaxIndex]} (${MaxProfit})
Greatest Decrease in Profits: {TotalMonths[MinIndex]} (${MinProfit})''')
