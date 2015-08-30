# Qonceptual Bluetooth scanner

import blescan
import sys
import time
import datetime

import bluetooth._bluetooth as bluez

dev_id = 0

try:
	sock = bluez.hci_open_dev(dev_id)
  	print "Qonceptual bleQon started"
	
except:
	print "That didnt work!!"
	sys.exxit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
# Set start values
TargetID=0

# Create a target list called Targets
Targets = {}
tCount=1


while True:
       
                # Set the noise floor for one minute
		bleTime=time.time()
		noiseTime= bleTime + 60
		print "Setting noise floor"
		while (bleTime < noiseTime):
			returnedList = blescan.parse_events(sock, 10)
			time.sleep(1)

         	
			for beacon in returnedList:

        			# Assign target ID based on tMAC
				# First we parse the comma delimited data
				# print beacon
				targetMAC, DATA, MAJOR, MINOR, RSSI, A = beacon.split(',')
                		curTime=datetime.datetime.now()
                		if targetMAC not in Targets:
					Targets[targetMAC] = tCount, curTime.isoformat(),RSSI
					#print "tMAC= %s c= %s time= %s rssi= %s" % (targetMAC, tCount, curTime, RSSI)
                                        #print "bleTime = ",bleTime
					tCount=tCount+1
			bleTime=time.time()
		print "Noise floor set at", tCount
		while True:
			returnedList = blescan.parse_events(sock, 10)
			time.sleep(1)
			for beacon in returnedList:

        			# Assign target ID based on tMAC
				# First we parse the comma delimited data
				# print beacon
				targetMAC, DATA, MAJOR, MINOR, RSSI, A = beacon.split(',')
                		curTime=datetime.datetime.now()
                		if targetMAC not in Targets:
					bleTime=time.time()
					Targets[targetMAC] = tCount, curTime.isoformat(),RSSI
					print "tMAC= %s c= %s time= %s rssi= %s" % (targetMAC, tCount, curTime, RSSI)
                                        print "bleTime = ",bleTime
					tCount=tCount+1

