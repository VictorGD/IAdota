# import csv
#
# cr = csv.reader(open("dota2.csv","rb"))
# for row in cr:
#     print(row)

import csv

with open("dota2.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
