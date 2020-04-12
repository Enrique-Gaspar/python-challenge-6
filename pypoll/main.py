# ------------------------------------------------------------------------------------------------
# Import dependencies 
# ------------------------------------------------------------------------------------------------
import os
import csv
from statistics import mean 
import numpy as np

# ------------------------------------------------------------------------------------------------
# Create a path 
# ------------------------------------------------------------------------------------------------
csvpath = os.path.join('resources','election_data.csv')
#print(csvpath)

# print()
# print('- - - - - - - - - - - - - - - - - - - - - - ')
# print('Election Results')
# print('- - - - - - - - - - - - - - - - - - - - - - ')

# Open the CSV module and read the file 
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header
    next(csv_reader)

    # ------------------------------------------------------------------------------------------------
    # Get the total number of votes cast
    # ------------------------------------------------------------------------------------------------
    votes_count = len(list(csv_reader))
    #print(f'Total Votes: {votes_count}')
    #print('- - - - - - - - - - - - - - - - - - - - - - ')

# ------------------------------------------------------------------------------------------------
# Get a list of candidates who received votes
# ------------------------------------------------------------------------------------------------
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    candidate_list = []
   
    for i in csv_reader:
        candidate = str(i[2])
        candidate_list.append(candidate)
    
    uc = np.unique(candidate_list)
    #print(uc) 
       
    candidate_one = str(uc[0]) 
    candidate_two = str(uc[1]) 
    candidate_three = str(uc[2]) 
    candidate_four = str(uc[3]) 
    #print(candidate_one) 


    count_one = 0
    count_two = 0
    count_three = 0
    count_four = 0
   
    for i in candidate_list:
        if i == candidate_one:
            count_one +=1
    
    #print(count_one)

    for i in candidate_list:
        if i == candidate_two:
            count_two +=1
    
    #print(count_two)

    for i in candidate_list:
        if i == candidate_three:
            count_three +=1
    
    #print(count_three)

    for i in candidate_list:
        if i == candidate_four:
            count_four +=1
    
    #print(count_four)

    perc_one = int((count_one * 100)/votes_count)
    perc_one_f = str('{:,.2f}%'.format(perc_one))
    #print(perc_one_f)
    perc_two = int((count_two * 100)/votes_count)
    perc_two_f = str('{:,.2f}%'.format(perc_two))
    perc_three = int((count_three * 100)/votes_count)
    perc_three_f = str('{:,.2f}%'.format(perc_three))
    perc_four = int((count_four * 100)/votes_count)
    perc_four_f = str('{:,.2f}%'.format(perc_four))

nl = '\n'

printable_results = (
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'{nl}'
    f'Election Results{nl}'
    f'{nl}'
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'Total Votes: {votes_count}{nl}'
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'{nl}'
    f'{candidate_one}:  {perc_one_f}  ({count_one}){nl}'
    f'{candidate_two}:  {perc_two_f}  ({count_two}){nl}'
    f'{candidate_three}:  {perc_three_f}  ({count_three}){nl}'
    f'{candidate_four}:  {perc_four_f}  ({count_four}){nl}'
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
    f'{nl}'
    f'Winner: {candidate_two}{nl}'
    f'{nl}'
    f'- - - - - - - - - - - - - - - - - - - - - -{nl}'
)

print(printable_results)

output_path = os.path.join('pypoll_analysis.txt')
with open(output_path, 'w') as txt_file:
    txt_file.write(printable_results)
    
