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
Single Domain check:

    python updown.py -d http://example.com
Repeated Domain check:   

    python updown.py -r http://example.com
    Once launched would ask for a number of times to repeat (0 for unlimited)
    Would also ask for delay between every scan

	
