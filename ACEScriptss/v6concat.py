import os, csv

path = os.getcwd()

files = os.listdir(path)

c_files = []

for file in files:
	if 'ip4-24' in file and '.csvv6' in file:
		v6_file = file[0:21]+'6-64'+file[25:-6]
		c_files.append((file, v6_file))

for item in c_files:
	file1 = open(item[0],'r')
	file2 = open(item[1],'r')
	file3 = open(item[1][0:-4]+'-IPV6.csv','w')

	csvfilereader1 = csv.DictReader(file1)
	csvfilereader2 = csv.DictReader(file2)
	headers = ['Ip','Total_Bytes','Country','Region Name','City','Zip','Latitude','Longitude','ISP','Org','ASNUM']
	csvwriter = csv.DictWriter(file3, fieldnames = headers)
	csvwriter.writeheader()
	
	for row in csvfilereader2:
		csvwriter.writerow(row)

	for row in csvfilereader1:
		csvwriter.writerow({'Ip':row['Ip'] ,'Total_Bytes':row['Total_Bytes'],'Country':row['Country'],'Region Name':row['Region Name'],'City' : row['City'],'Zip':row['Zip'],'Latitude':row['Latitude'],'Longitude':row['Longitude'],'ISP':row['ISP'],'Org':row['Org'],'ASNUM':row['ASNUM']})

	file1.close()
	file2.close()
	file3.close()

f_filenames = os.listdir(path)

for file in f_filenames:
	if '.csvv4s.' not in file and 'IPV6' not in file and '.py' not in file:
		os.system('rm '+file)
