import subprocess
import time
import sys

# will have to change commands based on location of data and based on the months.
# this is in parallel, leave the process.communicate as commented

# popen opens all the threads in parallel


def run_method():
    startTime = time.time()
    
    quarter=sys.argv[1]
    cPath="/home/asampath/IPDomainMap/Lib/httpclient-4.0.3.jar:/home/asampath/IPDomainMap/Lib/apache-httpcomponents-httpcore.jar:/home/asampath/IPDomainMap/src/:/home/asampath/IPDomainMap/Lib/commons-logging-1.2/commons-logging-1.2.jar:/home/asampath/IPDomainMap/Lib/sqlserverjdbc.jar:/home/asampath/IPDomainMap/Lib/mysql-connector-java-5.1.41-bin.jar"
    command = "cd /home/asampath/IPDomainMap/src/;pwd"
   
    process1 = subprocess.Popen(command, shell=True)
    
    commandPwd = "pwd"
    process2 = subprocess.Popen(commandPwd)

    command1 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-eu-dstip4-24-ipAndBytes > euDst4"+quarter+".txt"
    #print("done command1")
    # process5 = "pwd"

    #command2 = 'javac IpDomainDBargs.java'

    #command3 = 'java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-'+quarter+'-top-eu-dstip4-24-ipAndBytes > euDst4'+quarter+'.txt'

    command4 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-eu-dstip6-64-ipAndBytes > euDst6"+quarter+".txt"

    command5 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-eu-srcip4-24-ipAndBytes > euSrc4"+quarter+".txt"

    command6 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-eu-srcip6-64-ipAndBytes > euSrc6"+quarter+".txt"

    command7 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-us-srcip4-24-ipAndBytes > usSrc4"+quarter+".txt"

    command8 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-us-srcip6-64-ipAndBytes > usSrc6"+quarter+".txt"

    command9 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-us-dstip4-24-ipAndBytes > usDst4"+quarter+".txt"

    command10 = "export CLASSPATH="+cPath+";javac IpDomainDBargs.java;java IpDomainDBargs /home/asampath/IPDomainMap/src/ace-"+quarter+"-top-us-dstip6-64-ipAndBytes > usDst6"+quarter+".txt"



    process3 = subprocess.Popen(command1, shell=True)
    # process3 = subprocess.check_output('cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/2016/;nfdump -M 09:10:11 -R . -o csv -A dstip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> /home/asampath/ACE/Y7Q3/ace-Y7Q3-top-us-dstip4-24-ipAndBytes',shell=True)
    # results = str(process.read())
    #out,err = process3.communicate()
    #print("class path set",process3)

    process4 = subprocess.Popen(command9, shell=True)
    # process4 = subprocess.check_output(command2,shell=True)
    #out,err = process4.communicate()
    #print("compiled successfully",process4)
    # results1 = str(process1.read())

    process5 = subprocess.Popen(command10, shell=True)
    # process5 = subprocess.check_output(command3,shell=True)
    # out,err = process5.communicate()
    # print(process5)
    # results2 = str(process2.read())

    process6 = subprocess.Popen(command4, shell=True)
    # process6 = subprocess.check_output(command4,shell=True)
    # out,err = process6.communicate()
    # print(process6)
    # results3 = str(process3.read())

    process7 = subprocess.Popen(command5, shell=True)
    # process7 = subprocess.check_output(command5,shell=True)
    # out,err = process7.communicate()
    # print(process7)

    process8 = subprocess.Popen(command6, shell=True)
    # process8 = subprocess.check_output(command6,shell=True)
    # out,err = process8.communicate()
    # print(process8)
    process9 = subprocess.Popen(command7, shell=True)
    # process9 = subprocess.check_output(command7,shell=True)
    # out,err = process9.communicate()
    # print(process9)

    # process10 = subprocess.Popen(command8,shell=True)
    process10 = subprocess.Popen(command8, shell=True)

    out, err = process10.communicate()
    print(process10)
    # print(results1)
    # print(results2)
    # print(results3)

    print("----time taken for completion----", (time.time() - startTime))


run_method()
