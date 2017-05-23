
# Top countries in african traffic based on AS number. Script very similar to ParseAS script
#


import pandas as pd
import numpy as np
from collections import defaultdict
import csv

# input file path
fileName="C:/Users/Abhi/Desktop/y2q2/Africa/AfricaDestonlywithDetails.csv"


tempdict = defaultdict(set)
with open(fileName, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Country'] not in tempdict.keys():
            tempdict[row['Country']] = set()
            tempdict[row['Country']].add(row['Org'])
        else:
            tempdict[row['Country']].add(row['Org'])

    tempdict["NontopCountry"].add("Others - Top10")

df = pd.read_csv(fileName, encoding = "ISO-8859-1")
df["ASNUM"] = df["ASNUM"].replace("null", "AS64555")
df["ASNUM"] = df["ASNUM"].replace(np.nan, "AS64557")
df = df[df.Ip != '0.0.0.0']


pivot_values = pd.pivot_table(df, index=["Country"], values=["Total_Bytes"], aggfunc=np.sum)
totalsum = df["Total_Bytes"].sum()
pivot_values_sorted=pivot_values.sort_values("Total_Bytes",ascending=False, kind='quicksort')



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
        if each is "NontopCountry":
            OrgToASDict[each]="All other Country"
        try:
            OrgToASDict[each]=tempdict[each]
        except KeyError:
            OrgToASDict["NontopCountry"]="All other Country"
            pass



print(AstoValuesDict)

#output file path
fileName1="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL-result-AllCountry-Dest.txt"


topCount=100
with open(fileName1, "w") as myfile:
        myfile.write("List of all African Country(Destination) in ACE traffic from March-1-2016 to November-30-2016")

        myfile.write("\n")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("----------------------------------------"+"\n")
        myfile.write("1. Country - Total bytes "+ "\n")
        myfile.write("2. Country - Percent of Bytes"+"\n")
        myfile.write("3. Country - Institution Mapping in the same order" + "\n")
        myfile.write("----------------------------------------"+"\n")
        myfile.write("\n")
        myfile.write("Country"+","+"Total_Bytes" + "\n" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            if topCount==20:
                break
            totalbytes=round(AstoBytes[key]/(1024*1024*1024*1024),2)
            myfile.write(key + "," + str(totalbytes)+" TBs" +"\n")
            topCount+=1
        myfile.write("------------------------------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")

        myfile.write("Country"+","+ "Percent" + "\n" + "\n")

        for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            if topCount==40:
                break
            KeyValue=round(AstoValuesDict[key],2)
            myfile.write(key + "," + str(KeyValue) + "\n")
            topCount+=1
        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")

        myfile.write("Countries"+","+"AS NUMBERS under this Institution"+ "\n" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            if topCount==60:
                break

            myfile.write(key + "\n" +str(OrgToASDict[key])+"\n")
            myfile.write("****************************"+"\n")
            topCount+=1

        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
