# import modules and name essential variables

import csv
import os
totalvotes = 0

#create dictionary for storing votes against candidate name

candvotes = {}

# assign filepath

election_data = os.path.join("Resources/election_data.csv")

# assign how to read

with open(election_data) as csvfile:
    election_data_csv = csv.reader(csvfile, delimiter=',')

# separate first row as headers

    election_data_header = next(election_data_csv)

# use for loop to look at each row

    for row in election_data_csv:

        #add one to total votes counter

        candname = str(row[2])
        totalvotes += 1

        #if vote is for an existing candidate, add one vote

        if candname in candvotes.keys():
            candvotes[candname] += 1
        
        #else, add the candidate to the dictionary

        else:
            candvotes.update({candname: 1})

    #print results
            
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalvotes))
    print("-------------------------")

    for key,value in candvotes.items():
        candperc = (value/totalvotes)*100
        print(key + ": "  + str(round(candperc,3)) + "% (" + str(value) + ")")

    winner = max(candvotes, key=candvotes.get)

    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")


    #output results to text file in /analysis

    outputfile = "analysis/election_analysis.txt"

    with open(outputfile, 'w') as output:
        
        print("Election Results", file=output)
        print("-------------------------", file=output)
        print("Total Votes: " + str(totalvotes), file=output)
        print("-------------------------", file=output)

        for key,value in candvotes.items():
            candperc = (value/totalvotes)*100
            print(key + ": "  + str(round(candperc,3)) + "% (" + str(value) + ")", file=output)

        winner = max(candvotes, key=candvotes.get)

        print("-------------------------", file=output)
        print("Winner: " + winner, file=output)
        print("-------------------------", file=output)