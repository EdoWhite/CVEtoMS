# CVEtoMS
Simple program to search for MS exploit code from CVE.


## Why
I created this simple script during a CTF from hackthebox. Using Windows Exploit Suggester i got lots of exploits, with the relative CVE number. Using this simple program i can easly get the MS code from CVE number.


## Usage
Usage: `python3 cvems.py -c CVE-2000-0053`
The CVE number must be formatted as the example (CVE-xxxx-xxxx).

## Example
`white@kali:~$ python3 cvems.py -c CVE-2000-0098
################################
#           WhiteZucca         #
#           CVE to MS          #
#          (2020-04-12)        #
################################

[+] Downloading table...
[+] Looking up...

[+] CVE-2000-0098 is:
[*] MS00-006`




