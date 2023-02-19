import pandas as pd

# Import input file containing data
df = open("input.csv", "r")

# list for each customer id
list_C231 = []
list_C865 = []
list_C409 = []

# Loop through the lines in the cvs file
for line in df:
    # split the lines into specific sections
    line = line.split(",")

    # Append corresponding data depending on customer id
    if ("C231" in line):
        list_C231.append(int(line[2]))
    if ("C865" in line):
        list_C865.append(int(line[2]))
    if ("C409" in line):
        list_C409.append(int(line[2]))

# function to get ending balance of a data list
def end_balance(list):
    sum = 0
    for num in list:
        sum += num
    return str(sum)

# function to get minimum balance of a data list
def min_balance(list):
    min_balance = max(list)
    sum = 0
    for num in list:
        sum += num
        if sum < min_balance:
            min_balance = sum
    return str(min_balance)

# function to get maximum balance of a data list
def max_balance(list):
    max_balance = min(list)
    sum = 0
    for num in list:
        sum += num
        if sum > max_balance:
            max_balance = sum
    return str(max_balance)


# Create output data table
data = {'CustomerID':  ['C231', 'C865', 'C409'],
        'MM/YYYY': ['11/2022', '11/2022', '11/2022'],
        'MinBalance':  [min_balance(list_C231), min_balance(list_C865), min_balance(list_C409)],
        'MaxBalance':  [max_balance(list_C231), max_balance(list_C865), max_balance(list_C409)],
        'EndingBalance':  [end_balance(list_C231), end_balance(list_C865), end_balance(list_C409)]}
df = pd.DataFrame(data)
print(df)

# create output solution as a csv file
df.to_csv('output.csv', index = False)
