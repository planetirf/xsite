import csv

f = open('test.csv')

email_list = []

csv_f = csv.reader(f)

for row in csv_f:
    email_list.append(row[1])
    print email_list


f.close()

print len(email_list) 
