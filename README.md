# upDowns

Python based script that checks if a certain website / a list of websites are online.
Detects Cloudflare protections. 

~ Made by #peanutButter for OpDDOSISIS

# Usage:
Two options avaliable:

    -t for checking a textfile
    -d for checking a single domain
	-r for repeating a check multiple times
Textfile check:

    python updown.py -t weblist.txt
Single domain check:

    python updown.py -d http://example.com
	
	python updown.py -r http://example.com
	It would ask you how much times do you want (0 times = Infinite) to repeat the scan and how much delay do you want between each scan.
	After getting both of those it would output the results.
