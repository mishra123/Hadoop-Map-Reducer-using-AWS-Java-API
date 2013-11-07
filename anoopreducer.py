#!/usr/bin/python

import sys
import re

def main(argv):

	(last_word, sum, date) = (None, 0, '00000000')
	(sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9, sum_10, sum_11, sum_12, sum_13, sum_14, sum_15, sum_16, sum_17, sum_18, sum_19, sum_20, sum_21, sum_22, sum_23, sum_24, sum_25, sum_26, sum_27, sum_28, sum_29, sum_30) = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	for line in sys.stdin:
		(cur_word, value, cur_date) = line.strip().split( )
		if(last_word == cur_word and '20130601' == cur_date):
			(sum_1, date, last_word) = (int(value) + sum_1, cur_date , cur_word)	
		if(last_word == cur_word and '20130602' == cur_date):
			(sum_2, date, last_word) = (int(value) + sum_2, cur_date , cur_word)
		if(last_word == cur_word and '20130603' == cur_date):
			(sum_3, date, last_word) = (int(value) + sum_3, cur_date , cur_word)	
		if(last_word == cur_word and '20130604' == cur_date):
			(sum_4, date, last_word) = (int(value) + sum_4, cur_date , cur_word)	
		if(last_word == cur_word and '20130605' == cur_date):
			(sum_5, date, last_word) = (int(value) + sum_5, cur_date , cur_word)	
		if(last_word == cur_word and '20130606' == cur_date):
			(sum_6, date, last_word) = (int(value) + sum_6, cur_date , cur_word)	
		if(last_word == cur_word and '20130607' == cur_date):
			(sum_7, date, last_word) = (int(value) + sum_7, cur_date , cur_word)	
		if(last_word == cur_word and '20130608' == cur_date):
			(sum_8, date, last_word) = (int(value) + sum_8, cur_date , cur_word)	
		if(last_word == cur_word and '20130609' == cur_date):
			(sum_9, date, last_word) = (int(value) + sum_9, cur_date , cur_word)	
		if(last_word == cur_word and '20130610' == cur_date):
			(sum_10, date, last_word) = (int(value) + sum_10, cur_date , cur_word)	
		if(last_word == cur_word and '20130611' == cur_date):
			(sum_11, date, last_word) = (int(value) + sum_11, cur_date , cur_word)			
		if(last_word == cur_word and '20130612' == cur_date):
			(sum_12, date, last_word) = (int(value) + sum_12, cur_date , cur_word)	
		if(last_word == cur_word and '20130613' == cur_date):
			(sum_13, date, last_word) = (int(value) + sum_13, cur_date , cur_word)	
		if(last_word == cur_word and '20130614' == cur_date):
			(sum_14, date, last_word) = (int(value) + sum_14, cur_date , cur_word)	
		if(last_word == cur_word and '20130615' == cur_date):
			(sum_15, date, last_word) = (int(value) + sum_15, cur_date , cur_word)	
		if(last_word == cur_word and '20130616' == cur_date):
			(sum_16, date, last_word) = (int(value) + sum_16, cur_date , cur_word)
		if(last_word == cur_word and '20130617' == cur_date):
			(sum_17, date, last_word) = (int(value) + sum_17, cur_date , cur_word)	
		if(last_word == cur_word and '20130618' == cur_date):
			(sum_18, date, last_word) = (int(value) + sum_18, cur_date , cur_word)	
		if(last_word == cur_word and '20130619' == cur_date):
			(sum_19, date, last_word) = (int(value) + sum_19, cur_date , cur_word)	
		if(last_word == cur_word and '20130620' == cur_date):
			(sum_20, date, last_word) = (int(value) + sum_20, cur_date , cur_word)
		if(last_word == cur_word and '20130621' == cur_date):
			(sum_21, date, last_word) = (int(value) + sum_21, cur_date , cur_word)	
		if(last_word == cur_word and '20130622' == cur_date):
			(sum_22, date, last_word) = (int(value) + sum_22, cur_date , cur_word)	
		if(last_word == cur_word and '20130623' == cur_date):
			(sum_23, date, last_word) = (int(value) + sum_23, cur_date , cur_word)	
		if(last_word == cur_word and '20130624' == cur_date):
			(sum_24, date, last_word) = (int(value) + sum_24, cur_date , cur_word)	
		if(last_word == cur_word and '20130625' == cur_date):
			(sum_25, date, last_word) = (int(value) + sum_25, cur_date , cur_word)	
		if(last_word == cur_word and '20130626' == cur_date):
			(sum_26, date, last_word) = (int(value) + sum_26, cur_date , cur_word)	
		if(last_word == cur_word and '20130627' == cur_date):
			(sum_27, date, last_word) = (int(value) + sum_27, cur_date , cur_word)	
		if(last_word == cur_word and '20130628' == cur_date):
			(sum_28, date, last_word) = (int(value) + sum_28, cur_date , cur_word)	
		if(last_word == cur_word and '20130629' == cur_date):
			(sum_29, date, last_word) = (int(value) + sum_29, cur_date , cur_word)	
		if(last_word == cur_word and '20130630' == cur_date):
			(sum_30, date, last_word) = (int(value) + sum_30, cur_date , cur_word)	
		else: 
			sum = sum_1+ sum_2 + sum_3 + sum_4 + sum_5 + sum_6 + sum_7 + sum_8 + sum_9 + sum_10 + sum_11 + sum_12 + sum_13 + sum_14 + sum_15 + sum_16 + sum_17 + sum_18 + sum_19 + sum_20 + sum_21 + sum_22 + sum_23 + sum_24 + sum_25 + sum_26 + sum_27 + sum_28 + sum_29 + sum_30
	if last_word and sum_1 > 100000:
		print sum + '\t' + last_word + '\t' + str(sum) + '\t' + "date1:" + sum_1
	if last_word and sum_2 > 100000:
		print last_word + '\t' + "date2:" + sum_2	
	if last_word and sum_3 > 100000:
		print last_word + '\t' + "date3:" + sum_3
	if last_word and sum_4 > 100000:
		print last_word + '\t' + "date4:" + sum_4
	if last_word and sum_5 > 100000:
		print last_word + '\t' + "date5:" + sum_5
	if last_word and sum_6 > 100000:
		print last_word + '\t' + "date6:" + sum_6
	if last_word and sum_7 > 100000:
		print last_word + '\t' + "date7:" + sum_7
	if last_word and sum_8 > 100000:
		print last_word + '\t' + "date8:" + sum_8
	if last_word and sum_9 > 100000:
		print last_word + '\t' + "date9:" + sum_9
	if last_word and sum_10 > 100000:
		print last_word + '\t' + "date10:" + sum_10
	if last_word and sum_11 > 100000:
		print last_word + '\t' + "date11:" + sum_11
	if last_word and sum_12 > 100000:
		print last_word + '\t' + "date12:" + sum_12
	if last_word and sum_13 > 100000:
		print last_word + '\t' + "date13:" + sum_13
	if last_word and sum_14 > 100000:
		print last_word + '\t' + "date14:" + sum_14
	if last_word and sum_15 > 100000:
		print last_word + '\t' + "date15:" + sum_15
	if last_word and sum_16 > 100000:
		print last_word + '\t' + "date16:" + sum_16
	if last_word and sum_17 > 100000:
		print last_word + '\t' + "date17:" + sum_17
	if last_word and sum_18 > 100000:
		print last_word + '\t' + "date18:" + sum_18
	if last_word and sum_19 > 100000:
		print last_word + '\t' + "date19:" + sum_19
	if last_word and sum_20 > 100000:
		print last_word + '\t' + "date20:" + sum_20
	if last_word and sum_21 > 100000:
		print last_word + '\t' + "date21:" + sum_21	
	if last_word and sum_22 > 100000:
		print last_word + '\t' + "date22:" + sum_22
	if last_word and sum_23 > 100000:
		print last_word + '\t' + "date23:" + sum_23
	if last_word and sum_24 > 100000:
		print last_word + '\t' + "date24:" + sum_24	
	if last_word and sum_25 > 100000:
		print last_word + '\t' + "date25:" + sum_25
	if last_word and sum_26 > 100000:
		print last_word + '\t' + "date26:" + sum_26
	if last_word and sum_27 > 100000:
		print last_word + '\t' + "date27:" + sum_27
	if last_word and sum_28 > 100000:
		print last_word + '\t' + "date28:" + sum_28
	if last_word and sum_29 > 100000:
		print last_word + '\t' + "date29:" + sum_29
	if last_word and sum_30 > 100000:
		print last_word + '\t' + "date30:" + sum_30
		
		
if __name__ == "__main__":
	main(sys.argv)
