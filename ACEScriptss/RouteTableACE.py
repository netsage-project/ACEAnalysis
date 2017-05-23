fileName="rtr.seat.transpac.org v6 routing table.txt"
fileName1="RouterTableMap.txt"
file = open(fileName ,'r')
i=0
IpAsnum={}

for everyline in file:
    if i<10000:
        #print("line",i,"is")
        #print(eeryline)
        i+=1
        for each in everyline.split():
            if "::/" in each:
                subnet=each.rsplit(None,1)[-1]
                key=subnet
            if "AS_PATH:" in each:
                destAS=everyline.rsplit(None,1)[-1]
                print(i)
                print("prefix is",key)
                print("destAS is",destAS)


                value=destAS
                IpAsnum[key]=value


print(IpAsnum)
print(len(IpAsnum.keys()))


with open(fileName1, "w") as myfile:
    myfile.write("PREFIXES"+","+"ASNUM" + "\n")
    for key in sorted(IpAsnum):
        myfile.write(key + "," + IpAsnum[key] + "\n")
