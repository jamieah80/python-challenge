'''In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. 
The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.'''

# import modules and name essential variables

import csv
import os
totalrows = 0
totalprofit=0
prevrow=0
totalchange = 0
greatestincrease = 0
greatestdecrease = 0
change = 0

# assign filepath

budget_data = os.path.join("Resources/budget_data.csv")

# assign how to read

with open(budget_data) as csvfile:
    budget_data_csv = csv.reader(csvfile, delimiter=',')

    print(budget_data_csv)

# separate first row as headers

    budget_data_header = next(budget_data_csv)

# use for loop to look at each row

    for row in budget_data_csv:
        
    # find total rows (+1 to totalrows with each for loop)
    
        totalrows += 1

    # find sum of profits/losses (+row[1] to totalprofit for loop)
        
        totalprofit += int(row[1])
    
    # change = current row - previous row, add change to totalchange
        if prevrow != 0:
            change = int(row[1]) - prevrow
            totalchange += change

        #set prevrow for next loop
        prevrow = int(row[1])

        # compare change against greatestincrease and greatestdecrease, record row if its bigger or smaller
        if change > greatestincrease:
            greatestincrease = change
            incrmonth = row[0]
        
        if change < greatestdecrease:
            greatestdecrease = change
            decrmonth = row[0]


    # at end of loop, divide totalchange by totalrows to find average change. totalrows - 1 so we don't count the first row which does not have a change associated to it.
    
    averagechange = totalchange/(totalrows-1)


    # print values according to output example - ROUND FINANCIAL VALUES TO 2DP
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalrows))
    print("Total: " + "$" + str(round(totalprofit,2)))
    print("Average Change: " + "$" + str(round(averagechange,2)))
    print("Greatest Increase in Profits: " + incrmonth + " (" + str(greatestincrease) + ")")
    print("Greatest Decrease in Profits: " + decrmonth + " (" + str(greatestdecrease) + ")")

# create and write to .txt file in /analysis folder
        
outputfile = "analysis/budget_analysis.txt"

with open(outputfile, 'w') as output:
    
    print("Financial Analysis", file=output)
    print("----------------------------", file=output)
    print("Total Months: " + str(totalrows), file=output)
    print("Total: " + "$" + str(round(totalprofit,2)), file=output)
    print("Average Change: " + "$" + str(round(averagechange,2)), file=output)
    print("Greatest Increase in Profits: " + incrmonth + " (" + str(greatestincrease) + ")", file=output)
    print("Greatest Decrease in Profits: " + decrmonth + " (" + str(greatestdecrease) + ")", file=output)