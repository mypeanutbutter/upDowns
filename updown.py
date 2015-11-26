#!/usr/bin/python
# -*- coding: UTF-8 -*

# Made by peanutButter
# Made for Anonymous / #OpDDOSisis

from sys import argv
import sys
import time
import requests
import linecache
from urllib2 import Request, urlopen, HTTPError, URLError
import httplib
from time import localtime, strftime
from timeit import default_timer as timer
from os.path import exists

## Variables for counting, mainly for the textfile webcheck, the defined single target webcheck doesn't require it anymore.
up = 0 # Variable for amount of websites that are up in the scan
down = 0 # Variable for amount of websites that are down in the scan
crimeflare = 0 # Variable for amount of websites that are potentially protected by cloudflare (Error 403)

sprinklyline = "~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~" # Cus why not

## Welcome message
print sprinklyline
print("   upDowns, by peanutButter")
print("       Peanut Butter is tasty. yum.")
print sprinklyline

def scancomplete(): # Scan complete print
	print sprinklyline
	print("       Scan complete, Results are above!")
	print sprinklyline	

def scanresults(timerresult, timescale, down, up, crimeflare):
	print "Time taken to complete scan: ", timerresult, timescale
	print "Tangos down: ", down
	print "Up and running: ", up
	print "Potentially Cloudflare'd: ", crimeflare

if len(sys.argv) < 3: # If there's less than 3 arugments, ex: updown.py -t and no textfile selected / updown.py and no mode or textfile/ domain selected
	print("No options selected, Examples can be seen below:")
	print "Avaliable options for use:"
	print("      -d Domain -> For single website checks")
	print("      -t Textfile -> For a textfile with a bunch of websites")
	print sprinklyline

else:
	script, mode, target = argv

	def websitecheck(target):

		## Scan results count variables (function attributes)
		websitecheck.up = 0
		websitecheck.down = 0
		websitecheck.crimeflare = 0
		
		user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)' # User agent settings
		headers = { 'User-Agent':user_agent } # Headers
		req = Request(target, headers = headers) # Generate request

		## Single website check:
		try: # Try opening the target page
			page_open = urlopen(req)
		except HTTPError, e: # If there's an HTTP
			if e.code==403: # Check for error 403, mark as cloudflare and up
				print(target + u"\u2713" +" Is up! (Cloudflare?)")
				websitecheck.crimeflare += 1
				websitecheck.up += 1
			else: #Anything other than 403 = down
				print(target + u"\u2718" +" Is down! Error recieved : %s, %s") % (e.code, e.reason)
				websitecheck.down += 1
		except URLError, e: # If there's an URL error
			print(target + u"\u2718" +" Is down! : %s") % (e.reason)
			websitecheck.down += 1
		except httplib.HTTPException, e:
   			print(target + u"\u2718" +" Not sure? HTTP Exception")
		except Exception:
    			import traceback
    			print("Not sure, Generic exception while checking: " + target  + "(Connection reset by peer)")
		else: # If its up and all goes well
        		print(target + u"\u2713" +" Is up!")
			websitecheck.up += 1

	if mode == '-d': # If mode -d selected, domain check.
		
		## Timer
		start = timer() # Start scan timer
		
		## Single website scan
		websitecheck(target)
	
		print sprinklyline

		## Timer
		end = timer() # Stop scan timer
		timescale = 'seconds' # Set default scan timescale to seconds
		timerresult = end - start # Calculate time taken to complete scan
		if timerresult > 60: # Check if scan takes more than 60 seconds
			newtimerresult = timerresult / 60 # Div by 60 to get minutes
			timescale = 'minutes' # Change scan timescale to minutes, because we calculated minutes.
		else: # If scan doesn't take more than 60 seconds
			newtimerresult = timerresult # Change timer result to the original timer result.
		newtimerresult = int(newtimerresult) # Remove numbers after the decimal point

		scanresults(newtimerresult, timescale, websitecheck.down, websitecheck.up, websitecheck.crimeflare) # Prints scan results
		scancomplete() # Prints scan complete text

	if mode == '-r':
		numberoftimes = raw_input("Enter number of times you want the scan to be running (0 = Infinite) : ")
		delay = raw_input("Enter the delay you want between each scan (Recommended: 5) : ")
		print sprinklyline
		if numberoftimes == '0':
			print ("""You've selected infinite times,
you can press Ctrl + Z or Ctrl + C at any time to stop the scan.""")
			print sprinklyline
			count = 1
			while True: # Infinite loop
				print "Scan #", count # Show scan number
				websitecheck(target) # Scan target website
				time.sleep(int(delay)) # Apply selected delay
				count += 1
		else:
			print ("You will scan " + target + " " + numberoftimes + " times, with a delay of " + delay + " seconds between each scan, Starting scan:")
			print sprinklyline
			count = 0
			while (count < int(numberoftimes)): # Creates an infinite loop if you use numberoftimes without int, don't ask me how \o/
				print "Scan #", count + 1, "/Local time:", time.strftime("%H:%M:%S", localtime())
				websitecheck(target)
				time.sleep(int(delay))
				count += 1

	if mode == '-t': # If mode -t selected, textlist check.
		if bool(exists(target)): # Check if the textfile set as target actually exists
			txt = open(target) # Open text file specified
			print ("File information:")
			print "Text file selected: ", target # Prints the text file selected

			countlines = max(enumerate(open(target)))[0] # Returns number of lines minus 1
			lines = countlines + 1 # Add 1 to the line result, because ^

			print "Number of websites: ", lines # Returns number of websites in the text file (lines)
			print sprinklyline
			print ("Scan process:")
			print sprinklyline
			
			start = timer() # Start clock

			clinenum = 0 # Current line number
			while (clinenum<lines):	
				user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)' # User agent settings
				headers = { 'User-Agent':user_agent } # Headers
				line = open(target).readlines()[clinenum] # Open target and select line
				req = Request(line, headers = headers) # Generate request
				try: # Try opening the target page
					page_open = urlopen(req)
				except HTTPError, e: # If there's an HTTP
					if e.code==403: # Check for error 403, mark as cloudflare and up
						print(line + u"\u2713" +" Is up! (Cloudflare?)")
						crimeflare += 1
						up += 1
					else: #Anything other than 403 = down
						print(line + u"\u2718" +" Is down! Error recieved : %s, %s") % (e.code, e.reason)
						down += 1
				except URLError, e: # If there's an URL error
					print(line +u"\u2718" +" Is down! : %s") % (e.reason)
					down += 1
				except httplib.HTTPException, e:
   					print(line + u"\u2718" +" Not sure? HTTP Exception")
				except Exception:
    					import traceback
    					print("Generic exception while checking: " + line + "(Connection reset by peer)")
				else: # If its up and all goes well
        				print(line + u"\u2713" +" Is up!")
					up += 1
				print " " # Empty line for style
				clinenum += 1

			print sprinklyline

			## Timer
			end = timer() # Stop scan timer
			timescale = 'seconds' # Set default scan timescale to seconds
			timerresult = end - start # Calculate time taken to complete scan
			if timerresult > 60: # Check if scan takes more than 60 seconds
				newtimerresult = timerresult / 60 # Div by 60 to get minutes
				timescale = 'minutes' # Change scan timescale to minutes, because we calculated minutes.
			else: # If scan doesn't take more than 60 seconds
				newtimerresult = timerresult # Change timer result to the original timer result.
			newtimerresult = int(newtimerresult) # Remove numbers after the decimal point
			
			scanresults(newtimerresult, timescale, down, up, crimeflare) # Prints scan results
			scancomplete() # Prints scan completed text

		else: # If the textfile provided doesn't exist
			print ("The text file you set as target doesn't exist, wrong path?")
