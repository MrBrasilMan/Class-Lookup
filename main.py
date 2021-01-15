#By MrBrasilMan. Please see license.md for more
print ("Class Lookup")
import requests, os
from time import sleep
print ("____________________")
url = input ("Google Meet URL >")
while True:
  #Robj is what will be used to view information about the website using the request module. Cool, huh?
  robj = requests.get(url)
  print ("Pinging " + url)
  #A varaity of checks are done in order to verify that the URL is a valid, running Google Meet meeting before finally beeping or not.
  beepformeet = True
  if robj.status_code() != 200:
    beepformeet = False
  #This next bit is dependent on how Google Meet is structured. If a Google Meet is not available, it will go to a whoops error message only when an administrator has banned their class to create their own Google Meets.
  if "href=" in robj.text():
    pass