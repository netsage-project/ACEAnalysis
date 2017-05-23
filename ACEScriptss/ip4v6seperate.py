import socket
import pandas as pd
df = pd.read_csv('/home/aasingh/environments/ips/ace-y2q2-top-eu-srcip4-24-ipAndBytes-withASandDetails.csv', encoding = "iso-8859-1")
# Ip,Total_Bytes,Country,Region Name,City,Zip,Latitude,Longitude,ISP,Org,ASNUM
ipv4df=pd.DataFrame()
ipv6df=pd.DataFrame()
for ip in df.Ip:
    try:
        socket.inet_aton(ip)
        ipv4df = ipv4df.append(df[df.Ip==ip], ignore_index=True)
    except socket.error:
        ipv6df = ipv6df.append(df[df.Ip==ip], ignore_index=True)
        
ipv4df.to_csv("/home/aasingh/environments/ips/ace-y2q2-top-eu-srcip4-24-ipAndBytes-withASandDetailsipv4.csv")
ipv6df.to_csv("/home/aasingh/environments/ips/ace-y2q2-top-eu-srcip4-24-ipAndBytes-withASandDetailsipv6.csv")
