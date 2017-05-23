import socket
import pandas as pd
import sys


print ("filename is",sys.argv[1]);
filename=sys.argv[1];
#print ("year is",sys.argv[2]);
#year=sys.argv[2];

df = pd.read_csv('/home/aasingh/environments/ips/'+filename, encoding = "iso-8859-1")
# Ip,Total_Bytes,Country,Region Name,City,Zip,Latitude,Longitude,ISP,Org,ASNUM
ipv4df=pd.DataFrame()
ipv6df=pd.DataFrame()
for ip in df.Ip:
    try:
        socket.inet_aton(ip)
        ipv4df = ipv4df.append(df[df.Ip==ip], ignore_index=True)
    except socket.error:
        ipv6df = ipv6df.append(df[df.Ip==ip], ignore_index=True)
        
ipv4df.to_csv("/home/aasingh/environments/ips/"+filename+"v4s.csv")
ipv6df.to_csv("/home/aasingh/environments/ips/"+filename+"v6.csv")
