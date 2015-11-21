#!/usr/bin/python
# -*- coding: UTF-8 -*
from sys import argv
import sys
import requests
import linecache
from urllib2 import Request, urlopen, HTTPError, URLError
from colorama import Fore, Back, Style
from os.path import exists

script, mode, target = argv

print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")
print("   Check for online websites, by peanutButter")
print("       Peanut Butter is tasty. yum.")
print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")

up = 0 # Variable for amount of websites that are up in the scan
down = 0 # Variable for amount of websites that are down in the scan
cloudflare = 0 # Variable for amount of websites that are potentially protected by cloudflare (Error 403)

if len(sys.argv) == 1 or len(sys.argv) == 2: # If there's less than 3 arugments
	print(Fore.WHITE + "No options selected, Examples can be seen below:" + Style.RESET_ALL)
	print "	Options:"
	print "		-d Domain -> Check a domain, Example: 'python updown.py -d example.com'"
	print "		-t Text file -> Check a text file with domains (1 Domain in a line), Example: 'python updown.py -t websitelist.txt'"
else:
	if mode == '-d': # If mode -d selected, domain check.
		user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)' # User agent settings
		headers = { 'User-Agent':user_agent } # Headers
		req = Request(target, headers = headers) # Generate request

		try: # Try opening the target page
			page_open = urlopen(req)
		except HTTPError, e: # If there's an HTTP
			print(Fore.WHITE + target + Fore.RED + u"\u2718" +" Is down! Error recieved : %s, %s" + Style.RESET_ALL) % (e.code, e.reason)
			down += 1
		except URLError, e: # If there's an URL error
			print(Fore.WHITE + target + Fore.RED + u"\u2718" +" Is down! URL doesn't exist? : %s" + Style.RESET_ALL) % (e.reason)
			down += 1
		else: # If its up and all goes well
        		print(Fore.WHITE + target + Fore.GREEN + u"\u2713" +" Is up!" + Style.RESET_ALL)
			up += 1

		print "Number of websites down: ", down
		print "Number of websites up: ", up
		print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")
		print(Back.GREEN + Fore.WHITE +"       Scan complete "+Style.RESET_ALL+", Results are above!")
		print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")

	if mode == '-t': # If mode -t selected, textlist check.
		if bool(exists(target)): # Check if the textfile set as target actually exists
			txt = open(target) # Open text file specified
			print (Fore.WHITE + "File information:" + Style.RESET_ALL)
			print "Text file selected: ", target 

			countlines = max(enumerate(open(target)))[0] # Returns number of lines - 1
			lines = countlines + 1

			print "Number of websites: ", lines
			print "-----------------------------"
			print (Fore.WHITE + "Scan process:" + Style.RESET_ALL)

			clinenum = 0
			while (clinenum<lines):	
				user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)' # User agent settings
				headers = { 'User-Agent':user_agent } # Headers
				line = open(target).readlines()[clinenum]
				req = Request(line, headers = headers) # Generate request
				try: # Try opening the target page
					page_open = urlopen(req)
				except HTTPError, e: # If there's an HTTP
					if e.code==403: # Check for error 403, mark as cloudflare and up
						print(Fore.WHITE + line + Fore.GREEN + u"\u2713" +" Is up! (Cloudflare?)" + Style.RESET_ALL)
						cloudflare += 1
						up += 1
					else: #Anything other than 403 = down
						print(Fore.WHITE + line + Fore.RED + u"\u2718" +" Is down! Error recieved : %s, %s" + Style.RESET_ALL) % (e.code, e.reason)
						down += 1
				except URLError, e: # If there's an URL error
					print(Fore.WHITE + line + Fore.RED + u"\u2718" +" Is down! : %s" + Style.RESET_ALL) % (e.reason)
					down += 1
				else: # If its up and all goes well
        				print(Fore.WHITE + line + Fore.GREEN + u"\u2713" +" Is up!" + Style.RESET_ALL)
					up += 1
				clinenum += 1

			print "Number of websites down: ", down
			print "Number of websites up: ", up
			print "Number of websites potentially protected by Cloudflare: ", cloudflare
			print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")
			print(Back.GREEN + Fore.WHITE +"       Scan complete "+Style.RESET_ALL+", Results are above!")
			print("~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~")

		else:
			print (Fore.WHITE + "The text file you set as target doesn't exist, wrong path?" + Style.RESET_ALL)


#if len(sys.argv)==1:
#	print "Invalid domain"
#else:
#	try: 
#		urllib.urlopen('http://' + sys.argv[1]) 
#		print(Fore.WHITE + sys.argv[1] + Fore.GREEN + u"\u2713" +" Is up!")
#	except:
#   		print(Fore.RED + u"\u2718" +" Down")
