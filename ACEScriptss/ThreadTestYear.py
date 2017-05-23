import subprocess
import os
import time
import sys
def run_method():
        
	startTime= time.time()
	commandls="ls"
	
	
	print ("year1 is",sys.argv[1])
	year1=sys.argv[1]
	print ("year2 is",sys.argv[2])
	year2=sys.argv[2]
	print("path is",sys.argv[3])
	path=sys.argv[3]
	print("quarter title is",sys.argv[4])
	quarter=sys.argv[4]
	for arg in sys.argv:
		print("arg is",arg)

	month1="03:04:05:06:07:08:09:10:11:12"
	month2="01:02"	
	command = "cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/2016/;pwd"
        #month = "09"
	process = subprocess.Popen(commandls)
        #result = str(process.read())
        #print(result)
	print("done pwd")
	
	process1 = subprocess.Popen(command,shell=True)
	commandPwd= "pwd"
	process2 = subprocess.Popen(commandPwd)
	
	command1 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A dstip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-us-dstip4-24-ipAndBytes'
    	command11= 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A dstip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-us-dstip4-24-ipAndBytes'
	#print("done command1")
	#process5 = "pwd"
    	command2 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A dstip4/24 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-eu-dstip4-24-ipAndBytes'
    	command21 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A dstip4/24 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-eu-dstip4-24-ipAndBytes'

    	command3 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A srcip4/24 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-us-srcip4-24-ipAndBytes'
   	command31 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A srcip4/24 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-us-srcip4-24-ipAndBytes'

   	command4 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A srcip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-eu-srcip4-24-ipAndBytes'
   	command41 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A srcip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-eu-srcip4-24-ipAndBytes'

   	command5 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A dstip6/64 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-us-dstip6-64-ipAndBytes'
   	command51 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A dstip6/64 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-us-dstip6-64-ipAndBytes'
    	
    	command6 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A dstip6/64 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-eu-dstip6-64-ipAndBytes'
   	command61 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A dstip6/64 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 5,13 >> '+path+'/ace-'+quarter+'-top-eu-dstip6-64-ipAndBytes'
    
    	command7 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+'  -R . -o csv -A srcip6/64 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-us-srcip6-64-ipAndBytes'
    	command71 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+'  -R . -o csv -A srcip6/64 "in if 1 or in if 65 or in if 129" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-us-srcip6-64-ipAndBytes'

   	command8 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year1+';nfdump -M '+month1+' -R . -o csv -A srcip6/64 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-eu-srcip6-64-ipAndBytes'
   	command81 = 'cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/'+year2+';nfdump -M '+month2+' -R . -o csv -A srcip6/64 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 4,13 >> '+path+'/ace-'+quarter+'-top-eu-srcip6-64-ipAndBytes'
        

    	process3 = subprocess.Popen(command1,shell=True)
    	process31 = subprocess.Popen(command11,shell=True)
	#process3 = subprocess.check_output('cd /media/netflow/profiles-data/live/sw_wash_ace_iu_edu/2016/;nfdump -M 09:10:11 -R . -o csv -A dstip4/24 "in if 2 or in if 66 or in if 130" | cut -s -d , -f 5,13 >> /home/asampath/ACE/Y7Q3/ace-Y7Q3-top-us-dstip4-24-ipAndBytes',shell=True)
        #results = str(process.read())
	#out,err = process3.communicate()
        #print(process3)

    	process4 = subprocess.Popen(command2,shell=True)
    	process41 = subprocess.Popen(command21,shell=True)
	#process4 = subprocess.check_output(command2,shell=True)
	#out,err = process4.communicate()
        #print(process4)
        #results1 = str(process1.read())

   	process5 = subprocess.Popen(command3,shell=True)
    	process51 = subprocess.Popen(command31,shell=True)
	#process5 = subprocess.check_output(command3,shell=True)
    #out,err = process5.communicate()
        #print(process5)
	#results2 = str(process2.read())

    	process6 = subprocess.Popen(command4,shell=True)
    	process61 = subprocess.Popen(command41,shell=True)
	#process6 = subprocess.check_output(command4,shell=True)
	#out,err = process6.communicate()
        #print(process6)
        #results3 = str(process3.read())
	
	process7 = subprocess.Popen(command5,shell=True)
	process71 = subprocess.Popen(command51,shell=True)
	#process7 = subprocess.check_output(command5,shell=True)
	#out,err = process7.communicate()
        #print(process7)
        
	process8 = subprocess.Popen(command6,shell=True)
	process81 = subprocess.Popen(command61,shell=True)
	#process8 = subprocess.check_output(command6,shell=True)
	#out,err = process8.communicate()
        #print(process8)
	process9 = subprocess.Popen(command7,shell=True)
	process91 = subprocess.Popen(command71,shell=True)
	#process9 = subprocess.check_output(command7,shell=True)
	#out,err = process9.communicate()
        #print(process9)

	process10 = subprocess.Popen(command8,shell=True)
	process101 = subprocess.Popen(command81,shell=True)
	#process10 = subprocess.Popen(command8,shell=True)
        
	out,err = process101.communicate()
	print(process101)
        #print(results1)
        #print(results2)
        #print(results3)

	print("----time taken for completion----",(time.time()-startTime))



run_method()



