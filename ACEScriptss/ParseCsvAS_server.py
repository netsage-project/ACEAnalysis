import pandas as pd
import numpy as np
import csv
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
from collections import defaultdict
import os
import subprocess

def getMonthYearAndCommand(titlename):

    if "Q1" in titlename:
        month="March,April,May"
        year="2016"
    elif "Q2" in titlename:
        month="June,July,August"
        year="2016"
    elif "Q3" in titlename:
        month="September,October,November"
        year="2016"
    else:
        month="December,January,February"
        year="2016 and 2017"

    command="nfdump -M months -R . -o csv -A (srcip or dstip)(4/24 or 6/64) ('in if 1 or in if 65 or in if 129' or 'in if 2 or in if 66 or in if 130') " \
            "| cut -s -d , -f (4,13 or 5,13)"



    return year,month,command



def process(path,file,plt,titlename):

    #fileName1 = path+file+"-result.txt"
    #imageFile= path+file+".png"
    fileName1 = path+titlename+"-result.txt"

    #titlename='Y2Q2 -- TOP OUTGOING DESTINATION AS-NUMBERS FOR IPV4'

    tempdict = defaultdict(set)

    with open(filename, encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ASNUM'] not in tempdict.keys():
                tempdict[row['ASNUM']] = set()
                tempdict[row['ASNUM']].add(row['Org'])
            else:
                tempdict[row['ASNUM']].add(row['Org'])


    tempdict["NontopAS"].add("Others - Top10")
    #try:
        #for key,values in tempdict.items():
    #except UnicodeError:
        #pass

    #print(len(tempdict))

    df = pd.read_csv(filename)
    df["ASNUM"] = df["ASNUM"].replace("null", "AS64555")
    df["ASNUM"] = df["ASNUM"].replace(np.nan, "AS64557")
    df = df[df.Ip != '0.0.0.0']
    #print(df["ASNUM"].head(70))

    pivot_values = pd.pivot_table(df, index=["ASNUM"], values=["Total_Bytes"], aggfunc=np.sum)

    #print(pivot_values)

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
    AstoValuesDict["NontopAS"] = remainPercent

    remainBytes=totalsum-topsum
    AstoBytes["NontopAS"] = remainBytes

    labels = []
    labelValues = []
    for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
        if key is not "NontopAS":
            labels.append(key)
            labelValues.append(round(AstoValuesDict[key],1))
        else:
            NonASnumKey=key
            NonASval=round(AstoValuesDict[key],1)

    labels.append(NonASnumKey)
    labelValues.append(NonASval)
    
    detailedLabel=[]
    OrgNameForAsDict={}
    
    for each in labels:
        OrgName=getOrgNameForAS(each)
        OrgNameForAsDict[each]=OrgName
        value=each+"--"+str(OrgName)
        detailedLabel.append(value)	


    #print(len(labels))
    #print(len(labelValues))
    piechartDict={}

    for each in labels:
        if each is "NontopAS":
            piechartDict[each]="All other AS"
        try:
            piechartDict[each]=tempdict[each]
        except KeyError:
            piechartDict["NontopAS"]="All other AS"
            pass

    print("piechartdict is",piechartDict)

    sortedLegendLabel=[]

    for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            if key is not "NontopAS":
                sortedLegendLabel.append(key+"-"+OrgNameForAsDict[key]+"--"+str(round(AstoValuesDict[key],1)))
            else:
                NonASkey=key+"-"+str(OrgNameForAsDict[key])
                NonASValue=round(AstoValuesDict[key],1)
    sortedLegendLabel.append(NonASkey+"--"+str(NonASValue))

    piechartlist=[]
    for key,value in piechartDict.items():
        if key is "NontopAS":
            piechartlist.append("All other AS")
        if len(value)<=3:
            piechartlist.append(key+"->"+str(value))
        else:
            piechartlist.append(key+"->"+str(value.pop())+","+str(value.pop())+","+str(value.pop())+",.....")





    #print(AstoValuesDict)

    with open(fileName1, "w") as myfile:

        #myfile.write("Year and Month Details below" + "\n")
        year,month,command=getMonthYearAndCommand(titlename)
        myfile.write("Analysis for the year  " +year+ "  " + "during the months --- " +" " +month + "\n" )
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("Commad/Query "+ "\n" +command +"\n")
        myfile.write("\n")
        myfile.write("Command explained as below" +"\n")
        myfile.write("\n")

        #command="nfdump -M months -R . -o csv -A (srcip or dstip)(4/24 or 6/64) ('in if 1 or in if 65 or in if 129' or 'in if 2 or in if 66 or in if 130') " \
        #    "| cut -s -d , -f (4,13 or 5,13)"

        myfile.write("1. "+ "months to be replaced by digits based on quarter" +" (" + "For ex: " + "03:04:05 for Q1 or 05:06:07 for Q2" +" )" + "\n")
        myfile.write("2. "+"(srcip or dstip)" + " based on the source or destination" +"\n")
        myfile.write("3. "+"(4/24 or 6/64)" + " based on ipv4 prefixes or ipv6 prefixes"+ "\n")
        myfile.write("4. "+" For choosing "+" ('in if 1 or in if 65 or in if 129' or 'in if 2 or in if 66 or in if 130')" +
                     " We choose 'in if 1 or in if 65 or in if 129'" +
                     " if it is for outgoing traffic "+ " and " + "'in if 2 or in if 66 or in if 130'" +" if it is for outgoing traffic"+ "\n")
        myfile.write("5. "+ "Cut options" + " 4,13 for source AS" + " and 5,13 for destiation AS" +"\n")
        myfile.write("\n")

        myfile.write("----------------------------------------")
        myfile.write("\n")
        myfile.write("\n")




        myfile.write("ASNUM"+","+"Percent" + "\n")
        for key in sorted(AstoValuesDict, key=AstoValuesDict.get,reverse=True):
            #print(key)
            KeyValue=round(AstoValuesDict[key],2)
            myfile.write(key + "," + str(KeyValue) + "\n")

        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ASNUM"+","+"Total_Bytes" + "OrgName For AS" + "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            totalbytes=round(AstoBytes[key]/(1024*1024*1024), 2)
            myfile.write(key + "," + str(totalbytes)+" GBs"+ str(OrgNameForAsDict[key]) + "\n")


        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("ASNUM"+","+"Organisations under this AS NUM"+ "\n")
        for key in sorted(AstoBytes, key=AstoBytes.get,reverse=True):
            myfile.write(key + "," +str(piechartDict[key])+"\n")
            myfile.write("*********Next ASNUM***********"+"\n")



        myfile.write("--------------------------------------------------------------------------")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write("\n")
        myfile.write(pivot_values_sorted.to_string())
        myfile.write("\n")

    return detailedLabel,labels,labelValues,sortedLegendLabel

def plot(file,detailedLabel,labelsList,labelValues,titlename,sortedLegendLabel):
    #imageFile= file+".png"
    imageFile=path+titlename+".png"
    x = np.char.array(detailedLabel)
    y = np.array(labelValues)
    percent = 100.*y/y.sum()

    #colors = ['blue','green','red','cyan','magenta','yellow','gold','yellowgreen', 'lightcoral', 'lightskyblue','#FF5733']
    #colors = ['#F4D03F','#BA4A00','#48C9B0','#641E16','#F5B041','#EC7063','#1E8449','#F7DC6F','#633974','#AF601A',
    #          '#F5CBA7','#3498DB','#AAB7B8','#424949','#5499C7']

    colors = ['lightskyblue','maroon','salmon','greenyellow','crimson','fuchsia','darkorange','dimgrey','thistle','papayawhip','gold']

    explode = [0,0,0,0,0,0,0,0,0,0,0]  # explode 1st slice
    #patches, texts = plt.pie(labelValues, colors=colors, shadow=True, startangle=90)
    #patches, texts = plt.pie(labelValues,labels=detailedLabel, colors=colors, shadow=True, startangle=90)
    #patches, texts, autotexts = plt.pie(labelValues,autopct='%1.1f%%', shadow=True,colors=colors,radius=1.2,startangle=140,labeldistance=1.25)


    patches, texts, autotexts = plt.pie(labelValues,explode=explode,autopct='%1.1f%%', shadow=True,colors=colors,radius=1.7,startangle=90,labeldistance=1.25)


    plt.suptitle(titlename,bbox={'facecolor':'0.5', 'pad':15},y=1.28,fontsize=16)
    plt.legend(patches,sortedLegendLabel, loc="best", bbox_to_anchor=(-0.1, 1.),fontsize=14)

    plt.axis('equal')
    plt.tight_layout()
    fig = plt.gcf()
    fig.set_size_inches(13.5, 8.5)
    plt.tight_layout()
    fig.tight_layout()
    fig.savefig(imageFile, dpi=100,bbox_inches='tight')
    plt.clf()
    plt.cla()
    #plt.show()
    #plt.savefig(imageFile)

def title(file):
    #quarter="YQ2Q -- "
    quarter="ACE-"+"Y7Q3--"
    if "eu" in file:
        if "dst" in file:
            titlename=quarter+ "TOP10-OUTBOUND-DESTINATION-BY-ASNUMBERS"
        else:
            titlename=quarter+ "TOP10-INBOUND-SOURCE-BY-ASNUMBERS"
        if "6" in filename:
            titlename=titlename+"-FOR-IPV6"
        else:
            titlename=titlename+"-FOR-IPV4"
    else:
        if "dst" in file:
            titlename=quarter+ "TOP10-INBOUND-DESTINATION-BY-ASNUMBERS"
        else:
            titlename=quarter+ "TOP10-OUTBOUND-SOURCE-BY-ASNUMBERS"
        if "6" in file:
            titlename=titlename+"-FOR-IPV6"
        else:
            titlename=titlename+"-FOR-IPV4"

    return titlename

def getOrgNameForAS(label):

    asNum=label
    print("asnnum is",asNum)
    if asNum=="NontopAS":
        return

    output = subprocess.check_output('whois -h whois.cymru.com " -v ' + asNum + '">test.txt', shell=True)
    #output = subprocess.check_output('whois -h whois.cymru.com " -v AS23028">test.txt', shell=True)

    list = []
    f = open("test.txt", "r")
    for line in f:
    	list.append(line)

    tempList=[]
    for each in list[1].split("|"):
    	tempList.append(each)

    return tempList[4]


#path="C:/Users/Abhi/Desktop/y2q2/process-byAS/"
#path="C:/Users/Abhi/Desktop/finaly2q3/process-byAS/"
path="/home/asampath/dataForProcessing/y7q3/"
print("path is",path)

for filename in os.listdir(path):

    if filename.endswith(".csv"):

        print(os.path.join(path, filename))
        filename = path+filename
        file = filename[:-4]

        titlename=title(file)
        detailedLabel,label,labelValues,sortedLegendLabel=process(path,file,plt,titlename)


        print(titlename)

        plot(file, detailedLabel,label, labelValues, titlename,sortedLegendLabel)

