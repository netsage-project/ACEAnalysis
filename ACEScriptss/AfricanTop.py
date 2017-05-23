import pandas as pd
import numpy as np
from collections import defaultdict
import csv

# input file path
fileName="C:/Users/Abhi/Desktop/y2q2/Africa/AfricaDestonlywithDetails.csv"


tempdict = defaultdict(set)

with open(fileName, encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    validCount=0
    for row in reader:
        validCount+=1
        if row['ASNUM'] not in tempdict.keys():
            tempdict[row['ASNUM']] = set()
            tempdict[row['ASNUM']].add(row['Org'])
        else:
            tempdict[row['ASNUM']].add(row['Org'])


    print("row counter is",validCount)

    tempdict["NontopAS"].add("Others - Top10")



df = pd.read_csv(fileName, encoding = "ISO-8859-1")
df["ASNUM"] = df["ASNUM"].replace("null", "AS64555")
df["ASNUM"] = df["ASNUM"].replace(np.nan, "AS64557")
df = df[df.Ip != '0.0.0.0']

pivot_values = pd.pivot_table(df, index=["ASNUM"], values=["Total_Bytes"], aggfunc=np.sum)
totalsum = df["Total_Bytes"].sum()
pivot_values_sorted=pivot_values.sort_values("Total_Bytes",ascending=False, kind='quicksort')

TopTenAsNums=pivot_values_sorted.head(20)





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

print(AstoValuesDict)


AsToOrgDict={}
for each in AstoValuesDict.keys():
        if each is "NontopAS":
            AsToOrgDict[each]="All other AS"
        try:
            AsToOrgDict[each]=tempdict[each]
        except KeyError:
            AsToOrgDict["NontopAS"]="All other AS"
            pass


#output file path
fileName1="C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetailsALL-result-TopDestAS.txt"


with open(fileName1, "w") as myfile:
        myfile.write("Top Talkers in Africa based on Destination AS Numbers in ACE traffic from March-1-2016 to November-30-2016 ")
        #myfile.write("Top Talkers in US based on AS Numbers in ACE traffic from March-1-2016 to November-30-2016 ")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("----------------------------------------"+"\n")
        myfile.write("1. ASNUM - Percent of Bytes "+ "\n")
        myfile.write("2. ASNUM - Total bytes"+"\n")
        myfile.write("3. AS - ORG Mapping in the same order" + "\n")
        myfile.write("----------------------------------------"+"\n")

        myfile.write("ASNUM"+","+"Percent" + "\n")
        for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            #print("rep is",repr(key)
            KeyValue=round(AstoValuesDict[key],2)
            myfile.write(key + "," + str(KeyValue) + "\n")

        myfile.write("----------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ASNUM"+","+"Total_Bytes" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):

            totalbytes=round(AstoBytes[key]/(1024*1024*1024*1024),2)
            myfile.write(key + "," + str(totalbytes)+" TBs" + "\n")


        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ASNUM"+","+"Organisations under this AS NUM"+ "\n" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            myfile.write(key + "," +str(AsToOrgDict[key])+"\n")
            myfile.write("*********Next ASNUM***********"+"\n")


        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
