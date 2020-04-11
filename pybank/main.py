# ------------------------------------------------------------------------------------------------
# Import dependencies (os module to allow us to crete file paths across operating systems,
# and csv for reading csv files)
# ------------------------------------------------------------------------------------------------
import os
import csv
from statistics import mean 

# ------------------------------------------------------------------------------------------------
# Create a path (to tell Python where the file is, like a pointer), you can call it whatever you
# want, even when I chose 'csvpath' for clarity. 
# ------------------------------------------------------------------------------------------------
csvpath = os.path.join('resources','budget_data.csv')

# with open(csvpath, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
    
#     for line in csv_reader:
#         print(line)
#         # QQ you can also use print(line[1]) if you want only the second columns
#         # QQ if you want to get rid of the header, before the 'for loop' you have to add
#         # the 'next' function which will need the file name as a parameter
#         # for example: next(csv_reader)
print()
print('- - - - - - - - - - - - - - - - - - - - - - ')
print('Financial Analysis')
print('- - - - - - - - - - - - - - - - - - - - - - ')

# Open the CSV module and read the file 
with open(csvpath, 'r') as csv_file:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(csv_reader)

    # Read the first row as the header
    #header = next(csv_reader)
    #print(f'CSV Header: {header}')

    # Skip the header
    next(csv_reader)

    # ------------------------------------------------------------------------------------------------
    # Get the total number of months included in the dataset
    # ------------------------------------------------------------------------------------------------
    month_count = len(list(csv_reader))
    print(f'Total Months: {month_count}')

# ------------------------------------------------------------------------------------------------
# The net total amount of "Profit/Losses" over the entire period
# ------------------------------------------------------------------------------------------------
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    num_before = next(csv_reader)
    total = int(num_before[1])
    
    for line in csv_reader:
        total = total + int(line[1]) 
    
    print('Total: ' + str('${:,.2f}'.format(total)))


# ------------------------------------------------------------------------------------------------
# The average of the changes in "Profit/Losses" over the entire period
# ------------------------------------------------------------------------------------------------
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #header = next(csv_reader)
    first_row = next(csv_reader)
    #num_before = int(first_row[1])
    change_list = []
    current_row = 0
    diff_value = 0
    previous_numb = 0
    
    for line in csv_reader:
        current_row += 1
        if current_row == 1:
            previous_numb = int(line[1])
        else:
            diff_value = int(line[1]) - previous_numb
            previous_numb = int(line[1])
            change_list.append(diff_value)

    #print(change_list)
    print('Average Change: ' + str('${:,.2f}'.format(round(mean(change_list)))))

# ------------------------------------------------------------------------------------------------
# The greatest increase in profits (date and amount) over the entire period
# ------------------------------------------------------------------------------------------------
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    #num_before = next(csv_reader)
    amount_list = []
    month_list = []
    
    for line in csv_reader:
        number = int(line[1])
        amount_list.append(number)
        date = str(line[0])
        month_list.append(date)
        

    maximum_value = max(amount_list)
    #print(maximum_value)

    #print(amount_list)
    #print(month_list)
    zipped = zip(amount_list,month_list)

    best_month = ''
    for i in zipped:
        if i[0]== maximum_value:
            best_month = i[1]
            #print(best_month)
    
# ------------------------------------------------------------------------------------------------
# The greatest decrease in losses (date and amount) over the entire period
# ------------------------------------------------------------------------------------------------

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    amount_list = []
    month_list = []
    
    for line in csv_reader:
        number = int(line[1])
        amount_list.append(number)
        date = str(line[0])
        month_list.append(date)
        
    minimum_value = min(amount_list)
    #print(minimum_value)
    #mv_abs = abs(minimum_value)
    #print(mv_abs)

    #print(amount_list)
    #print(month_list)
    zipped = zip(amount_list,month_list)

    worst_month = ''
    for x in zipped:
        if x[0]== minimum_value:
            worst_month = x[1]
            #print(worst_month)


print('Greatest Increase in Profits: ' + best_month + '   ' + '${:,.2f}'.format(maximum_value))
print('Greatest Decrease in Profits: ' + worst_month + '   ' + '${:,.2f}'.format(minimum_value)) 
print('- - - - - - - - - - - - - - - - - - - - - - ')

# Note for the reviewer: please note that the maximum amount in the list is
# $11,79,593, and not $1,926,159 as it is is the example provided in the homework instructions. 
# I triple checked and I'm sure my results are right, so I don't know why it is different to the
# solution proposed. It would be nice to know where the difference is or why. Thanks. 

# ------------------------------------------------------------------------------------------------
# Final step, print the analysis to the terminal and export a text file with the results
# ------------------------------------------------------------------------------------------------

nl = '\n'
total_f = str('${:,.2f}'.format(total))
#print(f'total= {total_f}')
change_list_f = str('${:,.2f}'.format(round(mean(change_list))))
#print(f'Average change: {change_list_f}')
maximum_value_f =  str('${:,.2f}'.format(maximum_value))
#print(f'Maximum: {maximum_value_f}')
minimum_value_f =  str('${:,.2f}'.format(minimum_value))
#print(f'Minimum: {minimum_value_f}')


printable_thing = (
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'Financial Analysis{nl}'
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'Total Months: {month_count} {nl}'
    f'Total: {total_f} {nl}'
    f'Average Change: {change_list_f} {nl}' 
    f'Greatest Increase in Profits: {best_month} {maximum_value_f} {nl}'
    f'Greatest Decrease in Profits: {worst_month} {minimum_value_f} {nl}'
    f'- - - - - - - - - - - - - - - - - - - - - - {nl}'
    )

#print(printable_thing)

output_path = os.path.join('pybank_analysis.txt')
with open(output_path, 'w') as txt_file:
    txt_file.write(printable_thing)
