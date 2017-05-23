import csv
import os

# initial file preperation and filtering of files. Naming has to controlled manually! Lots of scripts to help with
# small changes. Most of the code is self-explanatory and can be changed according to the requirement and the country
# or continent you want to work on!

def writetoFile(row,euflag):

    if euflag:
        filenameWrite = "C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetails_y2q2_AfricadatafromEuropedataAllQuarters.csv"
    else:
        filenameWrite = "C:/Users/Abhi/Desktop/y2q2/AfricanCountireswithDetails_y2q2_AfricadatafromUSdataAllQuarters.csv"


    #print("writing to file",filenameWrite)
    with open(filenameWrite, "a") as myfile:

        try:
            myfile.write(row['Ip'] + "," + row['Total_Bytes'] + "," + row['Country'] + "," + row['City'] + "," +
                         row['ISP'] + "," + row['Org'] + "," + row['ASNUM'] + "\n")
        except UnicodeEncodeError:
            pass


fileName = "C:/Users/Abhi/Desktop/y2q2/AfricanCountires.csv"
file = open(fileName, 'r')
i = 0
countryList = []

for everyline in file:
    # print("country is",everyline)
    countryList.append(everyline.strip())

print(countryList)

path = "C:/Users/Abhi/Desktop/y2q2/process-byORG/"
count = 0
for filename in os.listdir(path):
    eachCount = 0
    euflag=False
    if filename.endswith(".csv"):
        print(os.path.join(path, filename))
        filename = path + filename
        print("filename is", filename)

        if "eu" in filename:
            euflag=True

        # fileName1="C:/Users/Abhi/Desktop/y2q4/process-byORG/ace-y2q4-top-eu-dstip4-24-ipAndBytes-withASandDetailsv4.csv"
        with open(filename, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            print("------------------------------------------------------------------------------------------")
            for row in reader:
                if row['Country'] in countryList:
                    writetoFile(row,euflag)
                    count += 1
                    eachCount += 1
    print("Each count is", eachCount)
    # print(row['Country'])

print("count value is", count)
