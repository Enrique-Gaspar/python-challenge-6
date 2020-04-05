# ------------------------------------------------------------------------------------------------
# Import dependencies (os module to allow us to crete file paths across operating systems,
# and csv for reading csv files)
# ------------------------------------------------------------------------------------------------
import os
import csv

# ------------------------------------------------------------------------------------------------
# Create a path (to tell Python where the file is, like a pointer)
# ------------------------------------------------------------------------------------------------

csvpath = os.path.join('resources','budget_data.csv')


# Open the CSV module and read the file 
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #Read the first row as the header (QQ: no more syntax error, nice!)
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')

    # The total number of months included in the dataset
    month_count = len(list(csvreader))
    #print(month_count)

    # pl_list = list(csvreader)
    # print(pl_list)

# The net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    headerline = csvfile.next()
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])
    print(total)
    
    # row_count = 0
    # # column_value = 0
    # # sum_values_column = 0

    # for row in csvreader:
    #     row_count += int(row[1])
    # print(row_count)
        
    #     column_value = int(row[1])
    #     sum_values_column = (sum_values_column + column_value)
    
    # print(sum_values_column)

    # def sumRows(filename, header=False):
    # d ={}
    # with open(filename) as csvfile:
    #     headerline = csvfile.next()
    #     total = 0
    #     for row in csv.reader(csvfile):
    #         total += int(row[1])
    #     print(total)



    # row_list = []
    # #profit_value = 0
    # #profit_value_accumulated = 0

    # for row in csvreader:
    #     row_count += 1
    #     row_list.append(row_count)

    #     #profit_value = int(row[1])
    #     # profit_value_accumulated = (profit_value_accumulated + profit_value)
    #     print(row_list)


# ------------------------------------------------------------------------------------------------
# Now that the importing of the CSV file is done, the actual activity is the following:
# Your task is to create a Python script that analyzes the records to calculate each of the following:


# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# ------------------------------------------------------------------------------------------------

# Create a list to append the information that will be retrieved later 
#months_list = []












