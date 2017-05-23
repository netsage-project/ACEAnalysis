import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import os


def process(path,file,plt):

    fileName1 = file+"-result.txt"
    tempdict = defaultdict(set)

    with open(filename, encoding="utf8") as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if row['Org'] not in tempdict.keys():
                tempdict[row['Org']] = set()
                tempdict[row['Org']].add(row['ASNUM'])
             else:
                tempdict[row['Org']].add(row['ASNUM'])

    tempdict["NontopOrg"].add("Others - Top10")
    #try:
    #    for key,values in tempdict.items():
    #        print(key, tempdict[key])
    #except UnicodeError:
    #    pass


             #print(row['Ip'])

    #print(len(tempdict))

    df = pd.read_csv(filename)
    df["ASNUM"] = df["ASNUM"].replace("null", "AS64555")
    df["ASNUM"] = df["ASNUM"].replace(np.nan, "AS64557")
    df = df[df.Ip != '0.0.0.0']
    #print(df["ASNUM"].head(70))

    pivot_values = pd.pivot_table(df, index=["Org"], values=["Total_Bytes"], aggfunc=np.sum)
    #pd.option_context('display.max_rows', 10000)
    #rint(pivot_values)

    totalsum = 0
    totalsum = df["Total_Bytes"].sum()
    #print(totalsum)

    pivot_values_sorted=pivot_values.sort_values("Total_Bytes",ascending=False, kind='quicksort')
    TopTenAsNums=pivot_values_sorted.head(10)

    AstoValuesDict = {}
    AstoBytes={}
    topsum=0
    for index,each in TopTenAsNums.iterrows():
        topsum += each["Total_Bytes"]
        AstoValuesDict[index] = (each["Total_Bytes"]/totalsum)*100
        AstoBytes[index] = each["Total_Bytes"]

    remainPercent = ((totalsum-topsum)/totalsum)*100
    AstoValuesDict["NontopOrg"] = remainPercent

    remainBytes=totalsum-topsum
    AstoBytes["NontopOrg"] = remainBytes

    labels = []
    labelValues = []
    for key, values in AstoValuesDict.items():
        labels.append(key)
        labelValues.append(values)


    piechartDict={}
    for each in labels:
        if each is "NontopOrg":
            piechartDict[each]="All other Orgs"
        try:
            piechartDict[each]=tempdict[each]
        except KeyError:
            piechartDict["NontopOrg"]="All other Orgs"
            pass

    print("piechartdict is",piechartDict)

    sortedLegendLabel=[]
    for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            sortedLegendLabel.append(key)


    piechartlist=[]
    for key,value in piechartDict.items():
        if key is "NontopOrg":
            piechartlist.append("All other Orgs")
        if len(value)<3:
            piechartlist.append(key+"->"+str(value))
        else:
            piechartlist.append(key+"->"+str(value.pop())+","+str(value.pop())+","+str(value.pop())+",.....")


    #print(AstoValuesDict)

    with open(fileName1, "w") as myfile:
        myfile.write("ORG"+","+"Percent" + "\n")
        for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            #print("rep is",repr(key)
            KeyValue=round(AstoValuesDict[key],2)
            myfile.write(key + "," + str(KeyValue) + "\n")

        myfile.write("----------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ORG"+","+"Total_Bytes" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):

            totalbytes=round(AstoBytes[key]/(1024*1024*1024),2)
            myfile.write(key + "," + str(totalbytes)+" GBs" + "\n")

        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ORG"+","+"ASNUM's under this ORG"+ "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            myfile.write(key + "," +str(piechartDict[key])+"\n")
            myfile.write("*********Next ORG***********"+"\n")

        myfile.write("----------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("\n")
        #print(pivot_values_sorted.values)
        #numpyarray=pivot_values_sorted.values
        try:
            myfile.write(str(pivot_values_sorted))
        except UnicodeError:
            pass
        myfile.write("\n")

    return labels,labelValues,sortedLegendLabel,piechartlist

def plot(file,labels,labelValues,titlename,sortedLegendLabel,piechartlist):
    imageFile= file+".png"
    colors = ['#F4D03F','#BA4A00','#48C9B0','#641E16','#F5B041','#EC7063','#1E8449','#F7DC6F','#633974','#AF601A',
              '#F5CBA7','#3498DB','#AAB7B8','#424949','#5499C7']
    explode = [0,0,0,0,0,0,0,0,0,0,0]  # explode 1st slice
    patches, texts = plt.pie(labelValues, colors=colors, shadow=True, startangle=90)
    plt.pie(labelValues, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(titlename,bbox={'facecolor':'0.9', 'pad':5},loc='right')
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig(imageFile, dpi=100)
    plt.clf()
    plt.cla()
    #plt.show()
    #plt.savefig(imageFile)

def title(file):
    #quarter="YQ2Q -- "
    quarter="Y2Q3 -- "
    if "eu" in file:
        if "dst" in file:
            titlename=quarter+ "TOP OUTGOING DESTINATION ORGANISATION"
        else:
            titlename=quarter+ "TOP OUTGOING SOURCE ORGANISATION"
        if "6" in filename:
            titlename=titlename+" FOR IPV6"
        else:
            titlename=titlename+" FOR IPV4"
    else:
        if "dst" in file:
            titlename=quarter+ "TOP INCOMING DESTINATION ORGANISATION"
        else:
            titlename=quarter+ "TOP INCOMING SOURCE ORGANISATION"
        if "6" in file:
            titlename=titlename+" FOR IPV6"
        else:
            titlename=titlename+" FOR IPV4"

    return titlename

#path="C:/Users/Abhi/Desktop/y2q2/process-byORG/"
path="C:/Users/Abhi/Desktop/finaly2q3/process-byORG/"


for filename in os.listdir(path):

    if filename.endswith(".csv"):

        print(os.path.join(path, filename))
        filename = path+filename
        file = filename[:-4]

        label, labelValues,sortedLegendLabel,piechartlist=process(path, file,plt)

        titlename=title(file)
        print(titlename)

        plot(file, label, labelValues, titlename,sortedLegendLabel,piechartlist)


