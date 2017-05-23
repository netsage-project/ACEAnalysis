
# This script helps to separate out traffic of a particular country from all the quarterly data.


import csv
import os

def writetoFile(row):

    filenameWrite="C:/Users/Abhi/Desktop/y2q2/USA/src/UsaSourceY2q4.csv"

    # append mode as we did for 3 folders. Can place all files in one folder and simplify it further
    # and change mode to wrote mode.
    with open(filenameWrite, "a") as myfile:

        try:
            myfile.write(row['Ip']+","+row['Total_Bytes']+","+row['Country']+","+row['City']+","+
                     row['ISP']+","+row['Org']+","+row['ASNUM']+"\n")
        except UnicodeEncodeError:
            pass


# this file has a list of all african countries
fileName="C:/Users/Abhi/Desktop/y2q2/AfricanCountires.csv"
file = open(fileName,'r')
i=0
countryList=[]

for everyline in file:
    #print("country is",everyline)
    countryList.append(everyline.strip())

print(countryList)


# this has to be the path of folder which contains all the files you want to process
path="C:/Users/Abhi/Desktop/y2q4/process-byORG/"
count=0

# traverse through the directory of target input files
for filename in os.listdir(path):
    eachCount=0
    if filename.endswith(".csv") and 'src' in filename:
        print(os.path.join(path, filename))
        filename = path+filename
        print("filename is",filename)

        with open(filename, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            print("------------------------------------------------------------------------------------------")
            for row in reader:

                # this line is separate out traffic, if its a list of countries, make changes
                # to countryList. If its one country change the string "United States"


                #if row['Country'] in countryList:
                if row['Country'] == "United States":
                    # writes each selected record to a new output file which contains only records
                    # of a particular country or continent
                    writetoFile(row)
                    count+=1
                    eachCount+=1
    print("Each count is",eachCount)
        #print(row['Country'])

print("count value is",count)
