import csv
with open('D:\\20mca030\\Data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)