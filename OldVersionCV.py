#!/bin/python

import sys
import os
import subprocess

contentviews = ['ContentView1', 'ContentView2', 'ContentView3', 'ContentView4', 'ContentView5', 'ContentView6', 'ContentView7', 'ContentView8']
COUNT=0
LIMIT=7
LENGTH=len(contentviews)
while COUNT < LENGTH:
 print("\n Content View name:" + str(contentviews[COUNT])+ "\n")
 CV=contentviews[COUNT]
 WC=subprocess.check_output("hammer content-view version list --content-view " + CV + " --organization EXAMPLE.COM | awk '{print $6}'|cut -d '|' -f1 |sed '/^$/d'|wc -l ", shell=True).strip()
 DIFF = int(WC) - LIMIT
 if DIFF <= 0:
  print "\n Content View have minimum number of verions: " + str(LIMIT)
 else:
  list = []
  list = subprocess.check_output("hammer content-view version list --content-view " + CV + " --organization EXAMPLE.COM | awk '{print $6}'|cut -d '|' -f1 |sed '/^$/d'" "|" "tail " "-" +str (DIFF), shell=True).splitlines()
  print "List of CV version to be deleted..", list
  for items in list:
   print "Version: ",items
   os.system("hammer content-view version delete --version " + items + " --content-view " + CV +  " --organization EXAMPLE.COM")
 COUNT += 1
