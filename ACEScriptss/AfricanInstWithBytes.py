import csv
import pandas as pd
import numpy as np

# top african institution with traffic of each institution

fileName="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL.csv"
InstitutionList=set()
OrgASDict={}


df = pd.read_csv(fileName)
pivot_values = pd.pivot_table(df, index=["Org"], values=["Total_Bytes"], aggfunc=np.sum)


with open(fileName, encoding = "ISO-8859-1") as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             InstitutionList.add(row['Org'])
             if row['Org'] not in OrgASDict.keys():
                 OrgASDict[row['Org']]=row['ASNUM']

print(len(OrgASDict))

for key,value in OrgASDict.items():
    print(key,",",value)

filenameWrite="C:/Users/Abhi/Desktop/y2q2/AfricanCountiresAllInstitutions.txt"
with open(filenameWrite, "w") as myfile:
    myfile.write("List of all African Institutions in ACE traffic from March-1-2016 to November-30-2016 ")
    myfile.write("\n")
    myfile.write("\n")
    myfile.write("\n")
    #myfile.write("ORG"+"\t"+"ASNUM" + "\n")
    myfile.write("ORGNAMES ARE :" + "\n")

    for key,value in OrgASDict.items():
        #print(key,",",value)
        #myfile.write(key+"\t"+value+"\n")
        myfile.write(key + "\n")
    myfile.write("---------------------------------------------------------")
