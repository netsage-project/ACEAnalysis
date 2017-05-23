# PythonRepo
This has all python scripts for ACE analysis and threading scripts for nfdump queries for analysis


Small explanation of each Scripts : 

i) ThreadTestMonth.py and ThreadTestYear.py are to run on flowproc for all 8 nfdump queries in parallel for months and year respectively. 

ii) ips.py are to seperate ipv6 and ipv4 files from ipv4files which has combination and ipv4 and ipv6 records

iii) javaThreadDB.py runs all the 8 threads of IPDomainargs java code getting detils of AS and other details for initail(prefix,bytes) files

iv) ParseCsvorg.py and ParseCscAS_server.py are to process the final 8 files for quarterly/monthly/yearly analysis based on Org/AS number

v) cropfiles.sh is to remove first two lines and last two lines from the prefix,bytes file.

vi) v6concat.py concatenates seperated ipv6 records from ipv4 with the actual ipv6 records. 

v) Rest are all self-explanatory utility files which is for seperation of traffic based on countries/continents and grouping them all together. 




