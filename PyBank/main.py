import os
import csv

csvpath = os.path.join('Resources', 'budget_data')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    column_sum = 0
    profit_dict = {}
    profit_list = []
    profit_blist= [0]

    #placing csv data in dictionary so have referance for dates that had the greatest inc/dec in profit
    for row in csvreader:
        date = row[0]
        profit = float(row[1])
        profit_dict.update({date: profit})
        #print(profit_dict)
    
    #obtained Total Months and  net total amount of Profit/Losses over the entire period
    for pair in profit_dict:
        total_months  = sum(1 for pair in profit_dict)
        column_sum = sum(profit_dict.values())

#moved profits into separate list to see if i could do math on the values
    profit_list.extend(profit_dict.values())
    profit_blist.extend(profit_dict.values())
    #    print(profit_list)

    #    print(profit_dict.values())



#futile attemps to do math on lists
    # previous_i = 0
    # change_list = []
    # for i in profit_list:
    #     # print(i)
    #     change = (i - previous_i) 
    #     previous_i = i

    
        

#printing results to terminal 
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${column_sum}')



#placing results in list and printing to text file 
result_list = ['Financial Analysis', '----------------------------', f'Total Months: {total_months}', f'Total: ${column_sum}']
file = open('Financial Analysis.txt', 'w')
for i in result_list:
    file.write(i)
    file.write("\n") 

file.close()