import os
import sys
import subprocess


#Lists (blank)
wifi_files = []
wifi_name = []
wifi_password = []

#Use Python to execute the 'netsh' Windows command
command = (["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#Grab the current direcroty
path = os.getcwd()

#Here are the hackies sh*t happen
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x,y in zip(wifi_name, wifi_password):
                            print("SSID: "+x, "Password: "+y, sep='\n')
            #Removing the hackies files
            try:
                os.remove(i)
            except:
                print("Error while deleting exported file")
