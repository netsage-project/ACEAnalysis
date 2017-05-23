from collections import defaultdict
import csv


# This script generates a dictionary of AS number to list of all prefixes under that AS number.
# This can be used as an input for AS-AS aggregation for some other scripts.


fileName="C:/Users/Abhi/Desktop/y2q2/USA/USADestonlywithDetails.csv"



tempdict = defaultdict(set)
with open(fileName, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['ASNUM'] not in tempdict.keys():
            tempdict[row['ASNUM']] = set()
            tempdict[row['ASNUM']].add(row['Ip'])
        else:
            tempdict[row['ASNUM']].add(row['Ip'])

print(len(tempdict))

