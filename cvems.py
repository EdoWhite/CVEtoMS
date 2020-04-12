#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import argparse

def search(cve):
    print("\033[1;33;40m[+] Downloading table...")
    tables=pandas.read_html("https://cve.mitre.org/data/refs/refmap/source-MS.html")
    print("\033[1;33;40m[+] Looking up...\n")
    cveTable=tables[3]
    for index, x in enumerate(cveTable[1]):
        for index1, y in enumerate(x.split(" ")):
            if y==cve:
                print("\033[1;31;40m[+] " + cve + " is:")
                out=cveTable[0][index].split(":")[1]
                print("\033[1;32;40m[*] " + out)
    return 0

parser = argparse.ArgumentParser(description='WhiteZucca CVE to MS')

parser.add_argument('-c',
                    metavar='cve',
                    type=str,
                    help='The CVE id to convert in MS id',
                    required=True)

args = parser.parse_args()

banner = "################################\n"
banner+= "#           WhiteZucca         #\n"
banner+= "#           CVE to MS          #\n"
banner+= "#          (2020-04-12)        #\n"
banner+= "################################\n"

print("\033[1;34;40m" + banner)

if args.c == None:
    print("Usage: python3 cvems.py -c CVE-2000-0053")
    exit()
else:
    cve=args.c;
    search(cve)
    print("\n")
    exit()        

