import pandas as pd
import numpy as np
from collections import defaultdict
import csv


# Script to indetify top organisations of african traffic


# input file path
fileName="C:/Users/Abhi/Desktop/y2q2/Africa/AfricaSourceonlywithDetails.csv"
#fileName="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL.csv"
#fileName="C:/Users/Abhi/Desktop/y2q2/USA/USonlywithDetails.csv"

tempdict = defaultdict(set)
with open(fileName, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Org'] not in tempdict.keys():
            tempdict[row['Org']] = set()
            tempdict[row['Org']].add(row['ASNUM'])
        else:
            tempdict[row['Org']].add(row['ASNUM'])

    tempdict["NontopOrg"].add("Others - Top10")

df = pd.read_csv(fileName, encoding = "ISO-8859-1")
df["ASNUM"] = df["ASNUM"].replace("null", "AS64555")
df["ASNUM"] = df["ASNUM"].replace(np.nan, "AS64557")
df = df[df.Ip != '0.0.0.0']


pivot_values = pd.pivot_table(df, index=["Org"], values=["Total_Bytes"], aggfunc=np.sum)
totalsum = df["Total_Bytes"].sum()
pivot_values_sorted=pivot_values.sort_values("Total_Bytes",ascending=False, kind='quicksort')

#TopTenAsNums=pivot_values_sorted.head(20)

TopTenAsNums=pivot_values_sorted



AstoValuesDict = {}
AstoBytes={}
topsum=0
for index,each in TopTenAsNums.iterrows():
    topsum += each["Total_Bytes"]
    AstoValuesDict[index] = (each["Total_Bytes"]/totalsum)*100
    AstoBytes[index] = each["Total_Bytes"]


print("topsum is",topsum)
remainPercent = ((totalsum-topsum)/totalsum)*100
AstoValuesDict["NontopAS"] = remainPercent
remainBytes=totalsum-topsum
AstoBytes["NontopAS"] = remainBytes


OrgToASDict={}
for each in AstoValuesDict.keys():
        if each is "NontopOrg":
            OrgToASDict[each]="All other Org"
        try:
            OrgToASDict[each]=tempdict[each]
        except KeyError:
            OrgToASDict["NontopOrg"]="All other Org"
            pass



print(AstoValuesDict)



#output file path
fileName1="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL-result-AllOrg-source.txt"
#fileName1="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL-result-AllOrg.txt"
#fileName1="C:/Users/Abhi/Desktop/y2q2/USA/USAwithDetailsALL-result-AllOrg.txt"
topCount=100
with open(fileName1, "w") as myfile:
        myfile.write("List of all African Institutions(Source) in ACE traffic from March-1-2016 to November-30-2016")
        #myfile.write("List of all American Institutions in ACE traffic from March-1-2016 to November-30-2016")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("----------------------------------------"+"\n")
        myfile.write("1. ORG - Total bytes "+ "\n")
        myfile.write("2. ORG - Percent of Bytes"+"\n")
        myfile.write("3. ORG - ASNUM Mapping in the same order" + "\n")
        myfile.write("----------------------------------------"+"\n")
        myfile.write("\n")
        myfile.write("ORG"+","+"Total_Bytes" + "\n" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            if topCount==20:
                break
            totalbytes=round(AstoBytes[key]/(1024*1024*1024*1024),2)
            myfile.write(key + "," + str(totalbytes)+" TBs" +"\n")
            topCount+=1
        myfile.write("------------------------------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")

        myfile.write("ORG"+","+ "Percent" + "\n" + "\n")

        for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            if topCount==40:
                break
            KeyValue=round(AstoValuesDict[key],2)
            myfile.write(key + "," + str(KeyValue) + "\n")
            topCount+=1
        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")

        myfile.write("Institution"+","+"AS NUMBERS under this Institution"+ "\n" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            if topCount==60:
                break

            myfile.write(key + "," +str(OrgToASDict[key])+"\n")
            myfile.write("*******"+"\n")
            topCount+=1

        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
