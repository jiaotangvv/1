# -*- coding:utf-8 -*-
import csv
import math
import sys
from datetime import date, time, datetime, timedelta

def Reader():
inputfile="C:\Users\TP\Desktop\1\time.csv"
	with open(inputfile,'r',newline='') as filereader:
		for row in filereader:
			if row[2].strip()==(''):
				starttime=time.strptime(row[1],"%H:%M:S")
				endtime=row[4]
				print(endtime-starttime).seconds
			
Reader()