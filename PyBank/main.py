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