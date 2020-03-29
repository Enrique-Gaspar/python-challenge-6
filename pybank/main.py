# First we'll import the os module to allow us to create file paths across operating systems
import os

# Second, import the module for reading CSV files
import csv

# Third, create a path (to tell Python where the file is, like a pointer)
csvpath = os.path.join('resources', 'budget_data.csv')

# Finally, open the CSV module and read the file 
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the first row as the header
    csv_header = next(csvreader)
    #Please note that if I try to print the following, I get a SyntaxError: Invalid syntax (???)
    #print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
        print(row)
